from socket import *


def smtp_client(port=1025, mailserver='127.0.0.1'):
    msg = "\r\n My message"
    endmsg = "\r\n.\r\n"

    # Create a socket called clientSocket and establish a TCP connection with the mailserver and port
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((mailserver, port))

    recv = clientSocket.recv(1024).decode()
    # Print the server's response
    # print(recv)

    #if recv[:3] != '220':
    #   print('220 reply not received from the server.')

    # Send HELO command and print server response.
    heloCommand = 'HELO Alice\r\n'
    clientSocket.send(heloCommand.encode())
    recv1 = clientSocket.recv(1024).decode()
    # print(recv1)

    # if recv1[:3] != '250':
    #   print('250 reply not received from the server.')

    # Send MAIL FROM command and handle server response.
    mail = 'MAIL FROM: arafat.ismail05@gmail.com\r\n'
    clientSocket.send(mail.encode())
    recv2 = clientSocket.recv(1024).decode()

    # Send RCPT TO command and handle server response.
    rcpt = 'RCPT TO: arafat111@aol.com\r\n'  
    clientSocket.send(rcpt.encode())
    recv3 = clientSocket.recv(1024).decode()

    # Send DATA command and handle server response.
    data = 'DATA\r\n'
    clientSocket.send(data.encode())
    recv4 = clientSocket.recv(1024).decode()

    # Send message data.
    clientSocket.send(msg.encode())

    # Message ends with a single period, send message end and handle server response.
    clientSocket.send(endmsg.encode())
    recv5 = clientSocket.recv(1024).decode()

    # Send QUIT command and handle server response.
    end = 'QUIT\r\n'
    clientSocket.send(end.encode())
    recv6 = clientSocket.recv(1024).decode()
   
    clientSocket.close()
