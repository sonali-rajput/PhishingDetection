# def emailInUrl(url):

import re
 
# Make a regular expression
# for validating an Email
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
 
# Define a function for
# for validating an Email
 
 
def check(email):
 
    # pass the regular expression
    # and the string into the fullmatch() method
    
    if(re.fullmatch(regex, email)):
        print("Valid Email")
        return 1 
 
    else:
        print("Invalid Email")
        return 0 

email_user= "sona1223@gmail.com"
print(check(email_user))