from cymruwhois import Client 
import whois 
import re 
import socket
import requests
import time
import os
from urllib.parse import urlparse
import urllib.request 
import dns.resolver
#import asn


class feature:



    def __init__(self,url):
        tempObj = urlparse(url)
        self.pt=tempObj.path
        head_tail = os.path.split(self.pt)
        self.filename= head_tail[1]
        self.directory = head_tail[0]
        self.nl=tempObj.netloc
        self.ht=tempObj.hostname
        self.url = url
        #self.prms=tempObj.params
        self.qry=tempObj.query 


    def asn(self,url):
        ip = socket.gethostbyname(url) 
        c = Client()
        r = c.lookup(ip)
        return r.asn


    def DirectoryLength(self,url):
        return os.path.basename(url)



    def DomainInIP(self,url):
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


    # def domainLength(self,url):
    #     return len(url)


    def emailInUrl(self,email):
        '''
        pass the regular expression and the string into the fullmatch() method
        '''
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+.[A-Z|a-z]{2,}\b'
        if(re.fullmatch(regex, email)):
            print("Valid Email")
            return 1 
        else:
            print("Invalid Email")
            return 0 


    def fileLength(self,url):
        # here a is the path of url
        return os.path.basename(url)


    # def LengthUrl(self,url):
    #     return len(url)


    def Length(self,url):
        return len(url)


    def qtyAndUrl(self,url):
        count = 0
        for i in url:
            if i=="&":
                count+=1
        return count



    # def searchingAsteriskDirectory(self,url):
    #     count = 0
    #     for i in url:
    #         if i=="*":
    #             count+=1
    #     return count 



    def searchingAsterisk(self,url):
        count = 0
        for i in url:
            if i=="*":
                count+=1
        return count 

    # def searchingAtDirectory(self,url):
    #     count = 0
    #     for i in url:
    #         if i=="@":
    #             count+=1
    #     return count 

    def searchingAt(self,url):
        count = 0
        for i in url:
            if i=="@":
                count+=1
        return count 

    def searchingComma(self,url):
        count = 0
        for i in url:
            if i==",":
                count+=1
        return count 

    def searchingDollar(self,url):
        count = 0
        for i in url:
            if i=="$":
                count+=1
        return count 

    #def searchingDotinDirectory(url):
    #    count = 0
    #    for i in url:
    #        if i==".":
    #            count+=1
    #    return count 

    def searchingDot(self,url):
        count = 0
        for i in url:
            if i==".":
                count+=1
        return count

    def searchingEqual(self,url):
        count = 0
        for i in url:
            if i=="=":
                count+=1
        return count 

    def searchingExclamation(self,url):
        count = 0
        for i in url:
            if i=="!":
                count+=1
        return count 

    def searchingHashtag(self,url):
        count = 0
        for i in url:
            if i=="#":
                count+=1
        return count 

    def searchingHyphen(self,url):
        count = 0
        for i in url:
            if i=="-":
                count+=1
        return count 


    def ipresolvecount(self,link):
        try:
            print(len(socket.gethostbyname(link)))
        except socket.gaierror:
            print(-1)

    
    def countmxservers(self,url):
        result = dns.resolver.query(url, 'MX')
        return len(result)


    def countnsservers(self,url):
        result = dns.resolver.query(url, 'NS')
        return len(result)


    def searchingPercent(self,url):
        count = 0
        for i in url:
            if i=="%":
                count+=1
        return count 

    def searchingQuestionMark(self,url):
        count = 0
        for i in url:
            if i=="?":
                count+=1
        return count 

    def countRedirects(self,url):
        responses = requests.get("https://forms.gle/hK9oHutvPAsnP3dAA")
        count = 0
        for response in responses.history:
            print(response.url)
            count+=1
        return count

    def searchingSlash(self,url):
        count = 0
        for i in url:
            if i=="/":
                count+=1
        return count 

    def searchingSpace(self,url):
        count = 0
        for i in url:
            if i==" ":
                count+=1
        return count 


    def searchingTilde(self,url):
        count = 0
        for i in url:
            if i=="`":
                count+=1
        return count 

    def lenthTldUrl(self,url):
        temp = url.split(".")
        return len(temp[2])


    def searchingUnderline(self,url):
        count = 0
        for i in url:
            if i=="_":
                count+=1
        return count 

    
    def CountVowels(self,url):
        count = 0
        for i in url:
            if i=="a" or i == "e" or i == "i" or i == "o" or i == "u":
                count+=1
        return count 

    def serverClientDomain(self,url):
    
        if url.find('server')!=-1 or url.find('client')!=-1:
            return 1
        return 0

    
    def is_registered(self,domain_name):
        """
        A function that returns a boolean indicating 
        whether a `domain_name` is registered
        """
        try:
            w = whois.whois(domain_name)
        except Exception:
            return False
        else:
            return bool(w.domain_name)
    
    def ssl(self,url):
        if "https" in url:
            return 1
        else:
            return 0

    def urlShort(self,url):
        
        def isWordPresent(link, word):
            k = 0
            h = 0
            for i in range(len(link)-1):
                if (link[i] == word[k]):
                    k += 1
                    if k>h:
                        h=k
                    if h == len(word):
                        return True
                else:
                    k = 0
            if h == len(word):
                return 1
            return 0

        lt = ["bit.ly","rebrand.ly","tinyurl.com","bl.ink","short.io"]
        for i in range(len(lt)):
            if isWordPresent(url,lt[i]):
                return 1



    def ttl_hostname(self,url):
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



    def timeResponse(self,url):

        dns_start = time.time()
        socket.gethostbyname(url)
        dns_end = time.time()
        return (dns_end - dns_start) * 1000


if __name__ == '__main__':
    object1 = feature("//www.cwi.nl:80/%7Eguido/Python.html?q=283928fjs")
    # lt = [object1.asn(object1.netloc),object1.]
    print(object1.nl)
    print(object1.ht)
    #print(object1.prms)
    print(object1.qry)
    print(object1.pt)
    print(object1.directory)
    print(object1.filename)
    lt = [
        object1.searchingQuestionMark(object1.directory),
        object1.emailInUrl(object1.url),
        object1.searchingDot(object1.filename),
        object1.searchingSlash(object1.url),
        object1.searchingDot(object1.directory),
        object1.searchingDot(object1.qry),
        object1.searchingEqual(object1.url),
        object1.searchingQuestionMark(object1.qry),
        object1.searchingUnderline(object1.directory),
        object1.searchingUnderline(object1.qry),
        object1.DirectoryLength(object1.directory),
        object1.qtyAndUrl(object1.url),

        
        ]


