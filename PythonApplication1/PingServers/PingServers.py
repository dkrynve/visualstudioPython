# -*- coding: utf-8 -*-
# Resolve Ip address list to Hostname!!!!!!
#Parameteres list of ip Address 
import socket
file = open("C:\\Users\\dkrynveniuk\\Documents\\ips.txt" ,"r")


for line in file:
    print (line),
    addr = socket.gethostbyaddr(line)
    print ('The address of ', line, 'is', addr)


hostname = 'maps.google.com'
addr = socket.gethostbyname(hostname)
print ('The address of ', hostname, 'is', addr)
