import socket as s 
import io

ipValidity = True
portValidity = True
nameValidity = True
userValidity = True
username = ""

#Checks if the ip is valid or not 
while(ipValidity):
    server_ip = input("You have the choice to either enter an IP address or press enter for localhost: ")
    #Option to enter for localhost, makes sure message is empty 
    if(server_ip==""):
        server_ip = "localhost"
        ipValidity = False
    else:
        #Option 2, to enter an ip themselves. Starts by splitting the ip.
        ipNums = [int(i) for i in server_ip.split(".") if i.isdigit()]
        #More tests to make sure that there is the possibilty of this being an actual legitimate ip
        if(len(ipNums) > 4 or len(ipNums) <4):
            print("You have not entered a valid IP address.\n")
            continue
        
        for x in range(len(ipNums)):
            if(ipNums[x] > 255 or ipNums[x] < 0):
                print("You must try again, the ip you entered is invalid.\n")
                break
            else:
                pass
        ipValidity = False 
        #Exits loop afterewards if no break or continue is encountered from an invalid method 
        
#Seeing if the server port is legitimate 
while(portValidity):
    server_port = input("Please enter a port number or press enter for a default port: ")
    if(server_port == ""):
        server_port = 8000
        portValidity = False
    else:
        server_port = int(server_port)
        if(server_port <= 1023):
            print("You have entered the wrong port number and you must try again.\n")
            continue
        else: 
            portValidity = False

#Checking for username validity
while(userValidity):
    client_username = input("Enter a username of choice: ")
    if(client_username == ""):
        print("You entered an invalid username, try again.n")
        continue
    else:
        userValidity = False
        
#Try statement to connect and start recieving/sending messages    
try:
    client_socket = s.socket(s.AF_INET, s.SOCK_STREAM)
    client_socket.connect((server_ip, server_port))
    print("Client is ready to recieve and send messages: ")
 
    while True:
        client_message = input("Enter chat: ")
        if (client_message == "end"):
            client_socket.send("end".encode())
            client_socket.close()
            break
 
        msg_to_server = client_username + ": " + client_message
        client_socket.send(msg_to_server.encode())  
        server_message = client_socket.recv(2048)  
        server_message = server_message.decode()
        
        if(server_message == "end"):
            client_socket.close()
            break
        
        print(server_message)
except:
    print("Socket could not connect or Error with sending/recieving Message. Ending program")
 