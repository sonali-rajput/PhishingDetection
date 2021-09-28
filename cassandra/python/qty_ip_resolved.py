import socket
def ipresolvecount(link):
    try:
        print(len(socket.gethostbyname(link)))
    except socket.gaierror:
        print(-1)
    
ipresolvecount("https://www.linkedin.com/")