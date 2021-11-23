def serverClientDomain(url):
    
    if url.find('server')!=-1 or url.find('client')!=-1:
        return 1
    return 0
    
# from urllib.parse import urlparse
url = 'http://www.exaservermple.com/si?te/secti?on1/.VAR1/VAR2' 
# urlparse(url)
# urlp = urlparse(url).path
# print(urlp)

print(serverClientDomain(url))