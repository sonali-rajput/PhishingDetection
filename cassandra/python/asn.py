from cymruwhois import Client
import socket


ip = socket.gethostbyname('google.com')

c = Client()
r = c.lookup(ip)
print(r.asn)


