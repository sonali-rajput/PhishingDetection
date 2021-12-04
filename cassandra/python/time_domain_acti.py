#we installed whois as pip install python-whois
import whois
from datetime import date
from datetime import datetime
def is_registered(domain_name):
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


#d0 = date(2008, 8, 18)
#d1 = date(2008, 9, 26)
#delta = d1 - d0
#print(delta.days)
    
# list of registered & non registered domains to test our function
domains = [
    "thepythoncode.com",
    "google.com",
    "github.com",
    "unknownrandomdomain.com",
    "notregistered.co"
]

# iterate over domains
# for domain in domains:
#     print(domain, "is registered" if is_registered(domain) else "is not registered")

# test with Google domain name
domain_name = "google.com"
def timeActivation(domain_name):
    if is_registered(domain_name):
        whois_info = whois.whois(domain_name)
        creationDate = whois_info.creation_date
        creationDate=[d.strftime('%m-%d-%Y') for d in creationDate]
        creationDate2=creationDate[0]
        datecreation = datetime.strptime(creationDate2, '%m-%d-%y')

        #expirationDate= date(whois_info.expiration_date
        #today = date.today()
        #activationDate = today - creationDate 
        #return activationDate.days 
        print(datecreation)

print(timeActivation(domain_name))