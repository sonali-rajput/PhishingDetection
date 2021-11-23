def searchingTldUrl(url):
    return len(url)

    
# from urllib.parse import urlparse
url = 'http://www.example.com/si?te/secti?on1/.VAR1/VAR2' 
# urlparse(url)
# urlp = urlparse(url).path
# print(urlp)

print(searchingTldUrl(url))