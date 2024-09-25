import socket
import time
import struct


def start_client(host='192.168.68.181', port=65433):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        print(f"Sending data to {host}:{port}")

        while True:
            # Example array of integers to send
            int_array = [1, 2, 3, 4, 5]
            # Convert the array of integers to bytes
            data = struct.pack(f'{len(int_array)}i', *int_array)
            # Send the byte data
            s.sendto(data, (host, port))
            print(f"Sent data: {int_array}")
            time.sleep(1)


#if _name_ == "__main__":
start_client()