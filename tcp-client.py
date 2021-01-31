###
# this does stuff and things
#
###
import logging
import socket

target_host = "127.0.0.1"
target_port = 9999

def makesocket():
    logger = logging.getLogger()

    #create a socket object
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #connect the client
    client.connect((target_host, target_port))

    #send some data
    client.send(b"GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")

    #receive some data
    response = client.recv(4096)

    print(response)
    logging.debug('End of makesocket()')

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s -  %(levelname)s -  %(message)s')
    logging.debug('Program run start...')
    makesocket()
    logging.debug('End of main...')



