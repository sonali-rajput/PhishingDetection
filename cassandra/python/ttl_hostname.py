import urllib.request 
f = None
try:
    f = urllib.request.urlopen('https://www.youtube.com/')

    header=str(f.headers)
    print(f.headers)
    result = header.find("max-age")
    answer=""
    j=0
    arr=[]
    i=result+8
    while(header[i]!="\n" and header[i]!=","):
        arr.append(header[i])
        i+=1
    ttl=list(map(int,arr))
    result = int("".join(str(i) for i in ttl),10)
    print(result)

except:
    result = None