def searchingHyphenDomain(url):
    count = 0
    for i in url:
        if i=="-":
            count+=1
    return count 

    
url = 'http://www.example.com/si?te/secti?on1/VAR1/VAR2' 
print(searchingHyphenDomain(url))