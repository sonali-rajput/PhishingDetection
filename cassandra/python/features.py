from cymruwhois import Client
import socket
import requests
import time
import os
from urllib.parse import urlparse
import urllib.request 
import dns.resolver


class feature:



    def __init__(self,url):
        self.pt=urlparse(url).path
        self.nl=urlparse(url).netloc
        self.prms=urlparse(url).params
        self.qry=urlparse(url).query 


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



    def searchingAsteriskUrl(self,url):
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

    def searchingAtUrl(self,url):
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

    def searchingHyphenDirectory(url):
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


    def searchingPercentDirectory(self,url):
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

    def searchingSlashParams(self,url):
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

    def searchingTldUrl(self,url):
        return len(url)


    def searchingUnderlineDomain(self,url):
        count = 0
        for i in url:
            if i=="_":
                count+=1
        return count 

    
    def searchingVowelsDomain(self,url):
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