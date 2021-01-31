###
# this does stuff and things
#
###
import logging
import socket

target_host = "127.0.0.1"
target_port = 80

def makesocket():
    logger = logging.getLogger()

    #create a socket object
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    #send some data
    client.sendto(b"AAABBBCCC", (target_host, target_port))

    #receive some data
    data, addr = client.recvfrom(4096)

    print(data)
    logging.debug('End of makesocket()')

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s -  %(levelname)s -  %(message)s')
    logging.debug('Program run start...')
    makesocket()
    logging.debug('End of main...')



