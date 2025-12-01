# servidor
<img width="273" height="164" alt="image" src="https://github.com/user-attachments/assets/439b3e59-8a30-412c-a4eb-db688acefab5" />

Este código primero importa socket, que sirve para manejar conexiones de red, y threading, que permite trabajar con varios clientes al mismo tiempo. Luego pongo HOST = "0.0.0.0" para que el servidor acepte conexiones desde cualquier red. Después creo la lista clientes, donde voy a guardar todas las conexiones de los usuarios que se conecten. Por último, hago lock = threading.Lock(), que básicamente es un seguro para evitar que varios hilos modifiquen la lista de clientes al mismo tiempo y el programa falle.

<img width="692" height="246" alt="image" src="https://github.com/user-attachments/assets/cef17eec-fef5-42f1-9b0c-902395076a06" />

Esta función básicamente se queda escuchando todo lo que envía el servidor. Entra en un ciclo infinito y cada vez intenta recibir datos del socket; si llega algo, lo decodifica y lo imprime tal cual. Si no llega nada, significa que el servidor cerró la conexión, entonces muestro un mensaje avisando y salgo del ciclo. Y si por alguna razón ocurre un error mientras recibe, simplemente rompo el ciclo también. En pocas palabras, esta función es la que mantiene al cliente leyendo los mensajes que vienen del servidor.

<img width="703" height="734" alt="image" src="https://github.com/user-attachments/assets/930e19d4-c9c0-418f-8ef3-c0f72afc1a1d" />

Esta función es básicamente la que se encarga de cada cliente que se conecta. Primero intento recibir el nombre del cliente; si no envía nada, cierro la conexión y salgo. Si sí envía un nombre, lo guardo en la lista de clientes usando el candado para evitar problemas con otros hilos. Luego mando un mensaje de bienvenida para avisar que ese usuario se conectó. Después entro en un ciclo donde voy recibiendo lo que escriba el cliente; si no llega nada o si escribe “/quit”, rompo el ciclo. Si llega un mensaje normal, lo reenvío a todos los demás usuarios con su nombre como prefijo. Si en todo este proceso pasa algún error, lo muestro, pero igual en el bloque finally saco al cliente de la lista, aviso que se desconectó y cierro la conexión. En pocas palabras, esta función controla toda la vida del cliente desde que entra hasta que se va.

<img width="866" height="404" alt="image" src="https://github.com/user-attachments/assets/9b22646c-c085-4c08-b233-872406e24c8d" />

Esta parte es básicamente el corazón del servidor: aquí creo el socket, le digo que use IPv4 y TCP, y activo la opción para reutilizar el puerto sin errores. Luego hago el bind para decirle en qué HOST y PORT debe escuchar, y con listen(5) lo pongo a esperar conexiones. Después entro en un ciclo infinito donde cada vez que un cliente se conecta hago un accept(), que me devuelve la conexión y la dirección. Inmediatamente creo un hilo nuevo para manejar a ese cliente con la función manejar_cliente, así no se bloquea el servidor atendiendo uno solo. Si paro el servidor con Ctrl+C, se captura el KeyboardInterrupt y muestro un mensaje de que se detuvo. Al final, pase lo que pase, cierro el socket. Y el bloque final solo ejecuta main() cuando corro el archivo directamente.

# cliente 
<img width="236" height="121" alt="image" src="https://github.com/user-attachments/assets/81a8cbc4-b616-4571-8306-8586d8032324" />

Aquí simplemente estoy importando lo que necesito: socket para poder conectarme al servidor, threading para poder escuchar mensajes sin que el programa se bloquee, y sys por si necesito leer argumentos o cerrar el programa. Luego defino las dos constantes básicas del cliente: SERVER_HOST, que en este caso es "localhost" porque me voy a conectar a mi propio PC, y SERVER_PORT, que es el puerto donde el servidor está escuchando, en este caso 5000. Con eso ya tengo listo el punto de conexión para el cliente.

<img width="544" height="201" alt="image" src="https://github.com/user-attachments/assets/f8f7db27-fa02-48d2-b96a-459451561072" />

Esta función básicamente se queda escuchando todo el tiempo lo que mande el servidor. Entra en un ciclo infinito y trata de recibir datos del socket; si el servidor no manda nada, significa que se cerró la conexión y por eso muestro un mensaje y salgo del ciclo. Si sí llega información, la imprimo tal cual decodificada, sin salto de línea extra para que se vea como un chat normal. Y si ocurre cualquier error mientras recibe, simplemente rompo el ciclo y dejo de escuchar. En esencia, esta función es el "oído" del cliente: está pendiente de todo lo que llega del servidor.

<img width="644" height="647" alt="image" src="https://github.com/user-attachments/assets/bea95617-29db-4f2d-87d7-a4cdb5a540b5" />

En esta función principal lo primero que hago es pedirle al usuario su nombre; si no escribe nada, simplemente no sigo. Luego creo el socket y trato de conectarme al servidor; si falla, muestro el error y salgo. Si sí me conecto, le mando al servidor mi nombre. Después arranco un hilo que se encarga de estar escuchando los mensajes que llegan del servidor, para que el programa no se bloquee. Luego entro en un ciclo donde leo lo que el usuario escribe; si escribe “/quit”, mando ese comando al servidor y cierro todo, y si escribe cualquier otra cosa, la mando con un salto de línea. Si el usuario cierra con Ctrl+C, lo capturo para no romper el programa. Al final, cierro el socket y muestro que se desconectó.

# funcionamiento
<img width="1429" height="531" alt="image" src="https://github.com/user-attachments/assets/b64b681a-e5c2-4a00-b902-e8f4fffbee56" />

Primero abrimos el servidor en una terminal

<img width="1490" height="360" alt="image" src="https://github.com/user-attachments/assets/0d8f0992-f3b7-46c7-8fd7-92f019c034d9" />

luego el cliente en otra terminal y escribimos nuestro nombre para poder conectarnos al servidor

<img width="1448" height="328" alt="image" src="https://github.com/user-attachments/assets/89a33a24-1178-4e42-8809-752ac85420e9" />

abrimos otra terminal y corremos otro cliente, cuando escribamos el nombre ya ambos estaran conectados al servidor y podran mandarse mensajes entre si

# Entre dos PC

para conectar el chat entre dos pc, primero que todo deben estar conectados a la misma red wifi,
luego debemos buscar el 
# HOST = "0.0.0.0" 
# SERVER_HOST = "localhost"
Y cambiar sus valores por el IP local IPv4
