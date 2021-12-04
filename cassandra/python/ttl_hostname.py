import urllib.request 
def ttl_hostname(url):
    f = None
    try:
        f = urllib.request.urlopen(url)

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
        return result 

    except:
        return 0