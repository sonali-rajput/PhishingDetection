from cymruwhois import Client
import socket

def asn(url):
    ip = socket.gethostbyname(url) 
    c = Client()
    r = c.lookup(ip)
    return r.asn 
url = "google.com"
print(asn(url))



