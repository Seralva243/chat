import socket
import threading

HOST = "0.0.0.0"   
PORT = 5000

clientes = []  
lock = threading.Lock()

def reenviar(mensaje, excluido_conn=None):
    """Enviar mensaje a todos los clientes excepto excluido_conn."""
    with lock:
        for conn, _ in clientes:
            if conn is not excluido_conn:
                try:
                    conn.send(mensaje.encode())
                except:
                    pass 
def manejar_cliente(conn, addr):
    try:
        nombre = conn.recv(1024).decode().strip()
        if not nombre:
            conn.close()
            return

        with lock:
            clientes.append((conn, nombre))

        bienvenida = f"[Servidor] {nombre} se ha conectado desde {addr}\n"
        print(bienvenida.strip())
        reenviar(bienvenida, excluido_conn=conn)

        while True:
            data = conn.recv(1024)
            if not data:
                break
            mensaje = data.decode().strip()
            if mensaje.lower() == "/quit":
                break
        
            reenviar(f"{nombre}: {mensaje}\n", excluido_conn=conn)

    except Exception as e:
        print("Error cliente:", e)
    finally:
        with lock:
            
            for i, (c, n) in enumerate(clientes):
                if c is conn:
                    clientes.pop(i)
                    break
        cierre = f"[Servidor] {nombre} se ha desconectado\n"
        print(cierre.strip())
        reenviar(cierre, excluido_conn=conn)
        conn.close()

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((HOST, PORT))
    s.listen(5)
    print(f"Servidor escuchando en {HOST}:{PORT}")

    try:
        while True:
            conn, addr = s.accept()
            thread = threading.Thread(target=manejar_cliente, args=(conn, addr), daemon=True)
            thread.start()
    except KeyboardInterrupt:
        print("\nServidor detenido.")
    finally:
        s.close()

if __name__ == "__main__":
    main()
