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
    

# test with Google domain name
domain_name = "www.youtube.com"
def timeActivation(domain_name):
    if is_registered(domain_name):
        whois_info = whois.whois(domain_name)
        creationDate = whois_info.creation_date
        #print(type(creationDate),"hi")
        if isinstance(creationDate,datetime):
            crd = creationDate
            crdate = crd.date()
            today = date.today()
            activationDate = today - crdate
            return activationDate.days

        if isinstance(creationDate,list):
            crd=creationDate[0]
            crdate = crd.date()
            today = date.today()
            activationDate = today - crdate
            return activationDate.days


def timeExpiration(domain_name):
    if is_registered(domain_name):
        whois_info = whois.whois(domain_name)
        expirationDate = whois_info.expiration_date

        if isinstance(expirationDate,datetime):
            erd = expirationDate
            expr = erd.date()
            today = date.today()
            exprDate = expr - today
            return exprDate.days
        if isinstance(expirationDate,list):
            erd=expirationDate[0]
            expr = erd.date()
            today = date.today()
            exprDate = expr - today
            return exprDate.days

        #type1=type(creationDate)
        # creationDate=[d.strftime('%m-%d-%Y') for d in creationDate]
        # creationDate2=creationDate[0]
        # datecreation = datetime.strptime(creationDate2, '%m-%d-%y')

        #expirationDate= date(whois_info.expiration_date
        #today = date.today()
        #print(today)
        #activationDate = today - creationDate 
        #return activationDate.days 
        #print(type1)

print(timeExpiration(domain_name))
print(timeActivation(domain_name))

