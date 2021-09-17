import socket
import time

hostname = 'www.google.com'

dns_start = time.time()
socket.gethostbyname(hostname)
dns_end = time.time()
print ('DNS time = ms' ,((dns_end - dns_start) * 1000) )