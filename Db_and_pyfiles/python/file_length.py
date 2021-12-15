import os
def fileLength(url):
    # here a is the path of url
    return os.path.basename(url)

url = 'http://www.exaservermple.com/si?te/secti?on1/.VAR1/VAR2' 

print(fileLength(url))