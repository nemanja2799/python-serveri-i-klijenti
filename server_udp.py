import socket
import struct

def start_server(host='192.168.68.181', port=65433, array_size=5):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.bind((host, port))
        print(f"Server listening on {host}:{port}")
        while True:
            data, addr = s.recvfrom(1024)  # 4 bytes per int
            if not data:
                break
            #int_array = struct.unpack(f'{array_size}i', data)
            print(f"Received data: {data.decode()}")

#if _name_ == "__main__":
start_server()