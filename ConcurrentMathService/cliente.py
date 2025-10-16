import socket

HOST = "127.0.0.1"
PORT = 5000

def run_client():
    print("Cliente conectado al servidor de operaciones matemáticas.")
    print("Formato: num1,num2,operacion (add, sub, mul, div)")
    print("Escribe 'quit' para salir.\n")

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.connect((HOST, PORT))
        except ConnectionRefusedError:
            print("❌ No se pudo conectar al servidor.")
            return

        while True:
            msg = input("Ingrese solicitud: ").strip()
            if not msg:
                continue
            s.sendall(msg.encode('utf-8'))

            if msg.lower() == "quit":
                print("👋 Cerrando conexión...")
                break

            data = s.recv(1024).decode('utf-8').strip()
            print("→ Respuesta del servidor:", data)

if __name__ == "__main__":
    run_client()
