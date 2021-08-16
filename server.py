#!/usr/bin/env python3
# Server Socket : 
# Listens on socket and displays the data received to stdout
import socket
import sys
import argparse

def server_echo(host,port):
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    s.listen()
    conn, addr = s.accept()
    with conn:        
        while True:
            data = conn.recv(5*1024)
            if not data:
                break
            print(data.decode("utf-8"),end='')
            


def main(args):
    parser = argparse.ArgumentParser(prog="server")
    parser.add_argument('-s',dest="server", nargs='?',default="0.0.0.0",
        help='Host Name ( 0.0,0,0) ')
    parser.add_argument('-p',dest="port", nargs='?',default="8080",
        help='port 8080')    
    args = parser.parse_args()           
    port = int(args.port)
    server_echo(args.server,port)              
    
if __name__ == "__main__":
   sys.exit(main(sys.argv[1:])) 