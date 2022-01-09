import whois 
import datetime
from datetime import date
def timeActivation(url):
        def is_registered(url):
            """
            A function that returns a boolean indicating 
            whether a `domain_name` is registered
            """
            try:
                w = whois.whois(url)
            except Exception:
                return False
            else:
                return bool(w.domain_name)
        if is_registered(url):
            whois_info = whois.whois(url)
            creationDate = whois_info.creation_date
            print(type(creationDate))
            #print(type(creationDate),"hi")
            if isinstance(creationDate,date):
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
