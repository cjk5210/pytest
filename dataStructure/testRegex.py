import re

def baseTestRegex(str):
    phoneNumRegex=re.compile(r'\d{3}\-\d{3}-\d{4}')
    mo=phoneNumRegex.search(str)
    print('Phone number has been found:',mo.group())

#baseTestRegex('My number is 415-555-4242')

def testWildCard():
    nongreedyRegex=re.compile(r'<.*?>')
    mo=nongreedyRegex.search('< To serve man> for dinner.>')
    print(mo.group())

    greedyRegex=re.compile(r'<.*>')
    mo=greedyRegex.search('< To serve man> for dinner.>')
    print(mo.group())
#testWildCard()

def testWildCardMatchWrap():
    noNelineRegex=re.compile('.*')
    mo=noNelineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.')
    print(mo.group())
    print('-------------------------')
    newLineRegex=re.compile('.*',re.DOTALL)
    mo=newLineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.')
    print(mo.group())
testWildCardMatchWrap()