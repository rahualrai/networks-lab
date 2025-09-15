import socket

HOST = '127.0.0.1'
PORT = 65432

try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        print(f"Connecting to {HOST}:{PORT}")
        client_socket.connect((HOST, PORT))
        print("Connected to server")
        
        message = input("Enter message to send: ")
        client_socket.sendall(message.encode('utf-8'))
        print(f"Sent: {message}")
        
        data = client_socket.recv(1024)
        response = data.decode('utf-8')
        print(f"Received: {response}")
        
        print("Disconnected from server")

except ConnectionRefusedError:
    print("Connection refused: Make sure the server is running")
except OSError as e:
    print(f"OS error: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
