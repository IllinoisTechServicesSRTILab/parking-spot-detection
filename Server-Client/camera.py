# following tutorial from https://www.geeksforgeeks.org/socket-programming-python/

# Import socket module 
import socket   

new_parking_spot = input("What parking spot is open: ")  
  
# Create a socket object 
s = socket.socket()          
  
# Define the port on which you want to connect 
port = 1233              
  
# connect to the server on local computer 
s.connect(('18.191.80.98', port)) 

# send data to the server 
s.sendall(bytes(new_parking_spot, 'utf-8'))
# close the connection 
s.close()  