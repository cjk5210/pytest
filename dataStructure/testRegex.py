import re

def baseTestRegex(str):
    phoneNumRegex=re.compile(r'\d{3}\-\d{3}-\d{4}')
    mo=phoneNumRegex.search(str)
    print('Phone number has been found:',mo.group())

baseTestRegex('My number is 415-555-4242')