from urllib.parse import urlparse 
url = 'http://www.example.com/site/section1/VAR1/VAR2' 
urlparse(url)
#ParseResult(scheme='http', netloc='www.example.com', path='/site/section1/VAR1/VAR2', params='', query='', fragment='')
print(urlparse(url).path)


