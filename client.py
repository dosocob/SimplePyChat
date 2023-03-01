import socket

def client_program(name, host, port):
     # Create a socket object 
     client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
     # Connect to the server 
     client_socket.connect((host, port)) 
     print(f"Connected to {host}:{port}") 
     
     while True:
        try:
            # Get input from the user
            message = input("Enter a message or type quit: ")
            if message == "quit":
                client_socket.close() 
                break
            # Send data to the server 
            message = f"{name}: {message}" 
            client_socket.send(message.encode('utf-8')) 
            # Receive data from the server 
            response = client_socket.recv(1024) 
            print(f"\n\nReceived: {response.decode('utf-8')}             \n\n") 
        except:
            print(".")

    # Close the connection 


if __name__ == '__main__':
   import sys
   
   if len(sys.argv) != 4:
       print("Usage: python client.py <name> <host> <port>")
       exit(1)

   name = sys.argv[1]
   host = sys.argv[2]
   port = int(sys.argv[3])

client_program(name, host, port)