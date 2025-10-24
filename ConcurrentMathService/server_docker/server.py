import socket
import threading

HOST = '0.0.0.0'  # ✅ Para Docker
PORT = 5000

def handle_client(conn, addr):
    print(f"[+] Cliente conectado desde {addr}", flush=True)  # ✅ flush=True agregado
    try:
        while True:
            data = conn.recv(1024).decode('utf-8').strip()
            if not data:
                break
            if data.lower() == "quit":
                print(f"[-] Cliente {addr} envió 'quit'.", flush=True)
                break

            parts = data.split(',')
            if len(parts) != 3:
                conn.sendall("ERROR: Formato inválido. Usa num1,num2,op\n".encode('utf-8'))
                continue

            try:
                num1 = float(parts[0])
                num2 = float(parts[1])
                op = parts[2].strip().lower()
            except ValueError:
                conn.sendall("ERROR: Números inválidos\n".encode('utf-8'))
                continue

            if op == "add":
                result = num1 + num2
            elif op == "sub":
                result = num1 - num2
            elif op == "mul":
                result = num1 * num2
            elif op == "div":
                if num2 == 0:
                    conn.sendall("ERROR: División por cero\n".encode('utf-8'))
                    continue
                result = num1 / num2
            else:
                conn.sendall("ERROR: Operación desconocida\n".encode('utf-8'))
                continue

            conn.sendall(f"RESULT:{result}\n".encode('utf-8'))
            print(f"[{addr}] {num1} {op} {num2} = {result}", flush=True)  # ✅ flush=True agregado

    except Exception as e:
        print(f"[ERROR] {addr}: {e}", flush=True)
    finally:
        conn.close()
        print(f"[-] Cliente desconectado: {addr}", flush=True)  # ✅ flush=True agregado

def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((HOST, PORT))
        s.listen()
        print(f"[*] Servidor escuchando en {HOST}:{PORT}", flush=True)  # ✅ flush=True agregado

        while True:
            conn, addr = s.accept()
            thread = threading.Thread(target=handle_client, args=(conn, addr))
            thread.daemon = True
            thread.start()

if __name__ == "__main__":
    start_server()
