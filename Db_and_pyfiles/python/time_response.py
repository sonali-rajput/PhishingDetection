import socket
import time

hostname = 'www.youtube.com'
def timeResponse(url):

    dns_start = time.time()
    socket.gethostbyname(url)
    dns_end = time.time()
    return (dns_end - dns_start) * 1000


print(timeResponse(hostname))