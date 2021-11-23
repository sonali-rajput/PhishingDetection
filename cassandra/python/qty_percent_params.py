def searchingPercentParams(url):
    count = 0
    for i in url:
        if i=="%":
            count+=1
    return count 

    
# from urllib.parse import urlparse
url = 'http://www.example.com/si?te/secti?on1/.VAR1/VAR2' 
# urlparse(url)
# urlp = urlparse(url).path
# print(urlp)

print(searchingPercentParams(url))