###
# a simple tcp server
#
###
import logging
import socket
import threading

bind_ip = "0.0.0.0"
bind_port = 9999

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((bind_ip, bind_port))
server.listen(5)

print("[*] Listening on %s:%d" % (bind_ip, bind_port))


def handle_client(client_socket):
    logger = logging.getLogger()
    #print what the client sends
    request = client_socket.recv(1024)
    print("[*] Received %s" % request)
    client.send(b"ACK!")
    print(client_socket.getpeername())
    client_socket.close()
    logging.debug('End of handle_client()')

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s -  %(levelname)s -  %(message)s')
    logging.debug('Program run start...')
    while True:
        client, addr = server.accept()
        print("[*] Accepted connection from %s:%d" % (addr[0],addr[1]))

        #spin up the client thread to handle incoming data
        client_handler = threading.Thread(target=handle_client,args=(client,))
        client_handler.start()

    logging.debug('End of main...')



