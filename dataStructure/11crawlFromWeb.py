import webbrowser,sys,pyperclip
#testkey，need copy into the clipboard:cjk--常佳康
def openWebbrowserWithUrlInTheClipBoard():
    word=pyperclip.paste()
    if len(word) > 1:
        webbrowser.open('https://www.baidu.com/s?word='+word)
#openWebbrowserWithUrlInTheClipBoard()
import requests
def requestsATXTFile():
    res=requests.get('http://www.gutenberg.org/cache/epub/1112/pg1112.txt')
    print(type(res))
    print(len(res.text))
    print(res.text[:250])
    res=requests.get('http://www.baidu.com')
    print(res.text[:100])
#requestsATXTFile()
def catchRequestsException():
    res=requests.get('http://inventwithpython.com/page_that_does_not_exist')
    try:
        res.raise_for_status()
    except Exception as exc:
        print('There are a problem:%s' % (exc))
#catchRequestsException()
def saveResponseTextIntoAFile():
    res=requests.get('http://www.gutenberg.org/cache/epub/1112/pg1112.txt')
    res.raise_for_status()
    playFile=open('RomeoAndJuliet.txt','wb')
    for chunk in res.iter_content(100000):
        playFile.write(chunk)
#saveResponseTextIntoAFile()