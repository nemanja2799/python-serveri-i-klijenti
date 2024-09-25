import socket
import struct

def start_server(host='192.168.68.181', port=65433, array_size=5):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()
        print(f"Server listening on {host}:{port}")
        conn, addr = s.accept()
        with conn:
            print(f"Connected by {addr}")
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                print(f"Received data: {data.decode()}")

#if _name_ == "__main__":
start_server()