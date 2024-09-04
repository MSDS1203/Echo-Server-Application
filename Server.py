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
    server_username = input("Enter a username of choice: ")
    if(server_username == ""):
        print("You entered an invalid username, try again.n")
        continue
    else:
        userValidity = False


try: 
     #Ready to start recieving connections and is just waiting 
    server_socket = s.socket(s.AF_INET, s.SOCK_STREAM)
    server_socket.bind((server_ip, server_port))
    server_socket.listen(1)
    print("Waiting for client, ready to recieve/send messages: ")
 
    #Client sent request and is just waiting to accept it
    connection_socket, addr = server_socket.accept()
 
    #Loop for sending messages until the loop is broken with "end"
    while True:
        client_message = connection_socket.recv(2048).decode()
        if(client_message == "end"):
            connection_socket.close()
            break
 
        print(client_message)
        server_message = input("Enter chat: ")
 
        if(server_message == "end"):
            connection_socket.send("end".encode())
            connection_socket.close()
            break
        else:
            msg_to_client = server_username + ": " + server_message
            connection_socket.send(msg_to_client.encode())
except:
    print("The program is ending because the socket could not connect")

        