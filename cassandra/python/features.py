from cymruwhois import Client
import socket
import os

class feature:
    def asn(self,url):
        ip = socket.gethostbyname(url) 
        c = Client()
        r = c.lookup(ip)
        return r.asn
    def DirectoryLength(self,url):
        return os.path.basename(url)
    def DomainInIP(url):
        try:
            obj = list(map(int,url.split(sep='.')))
            if len(obj)==4:
                for i in obj:
                    if(i>=0 and i<=255):
                        pass
                    else:
                        return 0
                return 1
            return 0
        except:
            return 0