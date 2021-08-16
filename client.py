#!/usr/bin/env python3
# client socket 
#         reads text from a file or stdin and sends it to server 
import socket
import sys
import argparse
import os



def client_connect(host,port,fh):
    try:
        s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, port))
        for data in fh:
            s.sendall(data.encode('utf-8'))
    except Exception as e:
        print(e)

def main(args):
    parser = argparse.ArgumentParser(prog="client")
    parser.add_argument('-s',dest="server", nargs='?',default="0.0.0.0",
        help='Host Name ( 0.0,0,0) ')
    parser.add_argument('-p',dest="port", nargs='?',default="8080",
        help='port 8080')
    parser.add_argument('-f',dest="fileName", nargs='?',default=None,
        help='[text file to read]: optional if not read from stdin')
    args = parser.parse_args()

    f = sys.stdin
    if(args.fileName):
        if os.path.isfile(args.fileName):
            f = open(args.fileName, "rt")           
    host=socket.gethostbyname(args.server)
    port = int(args.port)
    client_connect(host,port,f)                
    
if __name__ == "__main__":
   sys.exit(main(sys.argv[1:]))   


