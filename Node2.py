# Aditya Tripathi, Anurag Choudhury, Karan Sharma
# 2023 180 46, 2023 180 59, 2023 180 18
# MSc DS (Sem2)
import json
import socket
import threading
import numpy as np
###
def send_message(target_address, message):
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect(target_address)
        client_socket.send(json.dumps(message).encode('utf-8'))
        client_socket.close()
    except ConnectionRefusedError:
        print(f"Could not connect to {target_address}")
def matrix_multiply_part(matrix_part, other_matrix, result_shape):
    result_part = np.dot(matrix_part, other_matrix)
    return result_part.tolist()
def handle_client(client_socket, matrix_part, other_matrix, result_shape):
    data = client_socket.recv(1024).decode('utf-8')

    try:
        message = json.loads(data)
        if message['type'] == 'compute':
            result_part = matrix_multiply_part(matrix_part, other_matrix, result_shape)
            send_message((message['host'], message['port']), {'type': 'result', 'data': result_part})
    except json.JSONDecodeError:
        print("Invalid JSON received.")

    client_socket.close()
###
host = 'localhost'
port = 8002

matrix_part = np.array([[9, 10], [11, 12]])
other_matrix = np.array([[13, 14], [15, 16]])
result_shape = (2, 2)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen(5)

print(f"Node listening on {host}:{port}")

while True:
    client_socket, addr = server.accept()
    client_thread = threading.Thread(target=handle_client, args=(client_socket, matrix_part, other_matrix, result_shape))
    client_thread.start()