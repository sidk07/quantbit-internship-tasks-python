# Task 8 
# Extract email addresses from a text file. 

import re

def emailList(str) :
    # str = "Contact us at support@example.com or admin@example.org."
    str = str[:-1]
    txts = str.split()
    emails = []
    for i in txts :
        if re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', i) :
            emails.append(i)
    return emails
print(emailList("Contact us at support@example.com or admin@example.org."))