import socket
import threading

# A list to store all the connected client sockets
clients = []

def handle_client(client_socket):
    global clients # Use the global variable clients
    # Receive data from the client
    while True:
        try:
            request = client_socket.recv(1024)
            if not request:
                break # Connection closed by the client
            print(f"Received: {request.decode('utf-8')}")
            # Relay the message to all other clients
            for other_client in clients:
                if other_client != client_socket: # Don't send to self
                    other_client.send(request)
        except Exception as e:
            print(f"Error: {e}")
            break # Something went wrong
    
    # Remove the client from the list and close the connection
    clients.remove(client_socket)
    client_socket.close()


def server_program(port):
    global clients # Use the global variable clients
    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Get the hostname of this machine
    host = socket.gethostname()
    # Bind the socket to the port
    server_socket.bind((host, port))
    # Listen for incoming connections
    server_socket.listen(5)
    print(f"Server listening on {host}:{port}")
    
    while True:
        # Accept a connection from a client
        client_socket, address = server_socket.accept()
        print(f"Accepted connection from {address}")
        # Add the client to the list 
        clients.append(client_socket)
        # Create a thread to handle the client
        client_thread = threading.Thread(target=handle_client, args=(client_socket,))
        client_thread.start()

if __name__ == '__main__':
    import sys
    
if len(sys.argv) != 2:
   print("Usage: python server.py <port>")
   exit(1)

port = int(sys.argv[1])

server_program(port)