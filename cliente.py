import socket
import threading
import sys

SERVER_HOST = "localhost" 
SERVER_PORT = 5000

def escuchar(sock):
    while True:
        try:
            data = sock.recv(1024)
            if not data:
                print("[Conexión cerrada por el servidor]")
                break
            print(data.decode(), end="")
        except:
            break

def main():
    nombre = input("Tu nombre: ").strip()
    if not nombre:
        print("Debe ingresar un nombre.")
        return

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.connect((SERVER_HOST, SERVER_PORT))
    except Exception as e:
        print("No se pudo conectar al servidor:", e)
        return

    sock.send((nombre + "\n").encode())

    hilo = threading.Thread(target=escuchar, args=(sock,), daemon=True)
    hilo.start()

    try:
        while True:
            msg = input()
            if msg.strip().lower() == "/quit":
                sock.send("/quit".encode())
                break
            sock.send((msg + "\n").encode())
    except KeyboardInterrupt:
        pass
    finally:
        sock.close()
        print("Desconectado.")

if __name__ == "__main__":
    main()
