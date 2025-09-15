import socket

HOST = '127.0.0.1'
PORT = 65432

try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((HOST, PORT))
        server_socket.listen()
        print(f"Server listening on {HOST}:{PORT}")
        
        conn, addr = server_socket.accept()
        with conn:
            print(f"Connected by {addr}")
            
            data = conn.recv(1024)
            if data:
                message = data.decode('utf-8')
                print(f"Received: {message}")
                
                response = f"Echo from server: '{message}'"
                conn.sendall(response.encode('utf-8'))
                print(f"Sent: {response}")
            
            print("Connection closed")

except PermissionError:
    print("Permission denied: Cannot bind to the specified port")
except OSError as e:
    print(f"OS error: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
