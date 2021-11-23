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
    
# from urllib.parse import urlparse
url = 'http://www.exaservermple.com/si?te/secti?on1/.VAR1/VAR2' 
# urlparse(url)
# urlp = urlparse(url).path
# print(urlp)

print(DomainInIP(url))