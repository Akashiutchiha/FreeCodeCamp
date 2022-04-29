#In Networking.py i worked using Sockets, Now i will use urllib to do the
#Connection.  Urllib is a library used in python for implementing http
import urllib.request, urllib.parse, urllib.error
#importing useful libraries

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
#This line above creates the socket, sends the command  using the GET from 
#http, set the number of bits for our socket to recieve the data, deals with
#the encoding and stores the data in a variable called fhand

for line in fhand:
    print(line.decode())