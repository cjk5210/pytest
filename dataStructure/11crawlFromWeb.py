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
    playFile.close()
#saveResponseTextIntoAFile()
import bs4
def createAHTMLFile():
    ht=open('example.html','w')
    content="""
    <!-- This is the example. html example file. --> 
    <html>
        <head>
            <title> The Website Title</title>
        </head> 
        <body> 
            <p> Download my <strong> Python</strong> book from <a href="http://inventwithpython.com"> my website</a>.</p> 
            <p class="slogan"> Learn Python the easy way!</p>
            <p> By <span id="author"> Al Sweigart</span></ p> 
        </body>
    </html> 
    """
    ht.write(content)
    ht.close()
#createAHTMLFile()

def getTheTypeOfBs4():
    res=requests.get('https://www.baidu.com')
    res.raise_for_status()
    nosStarchSoup=bs4.BeautifulSoup(res.text,"html.parser")
    print(type(nosStarchSoup))

#getTheTypeOfBs4()
def analysisHtmlFileByBs4():
    createAHTMLFile()   #create html file
    exampleFile=open('example.html')
    exampleSoup=bs4.BeautifulSoup(exampleFile,"html.parser")
    print(type(exampleSoup))
#analysisHtmlFileByBs4()
def findTheElementFromHtmlByBs4WithSelectMethod():
    createAHTMLFile()  # create html file
    exampleFile=open('example.html')
    exampleSoup=bs4.BeautifulSoup(exampleFile,"html.parser")
    elems=exampleSoup.select('#author')
    print('1--',type(elems))
    print('2--',len(elems))
    print('3--',type(elems[0]))
    print('4--',elems[0].get_text())
    print('5--',str(elems[0]))
    print('6--',str(elems[0].attrs))
    pElems=exampleSoup.select('p')
    print('7--',str(pElems[0]))
    print('8--',pElems[0].getText())
    print('9--', pElems[0].get_text())
#findTheElementFromHtmlByBs4WithSelectMethod()
from selenium import webdriver
def openUrlBySeleniumWithFireFox():
    browser=webdriver.Firefox()
    type(browser)
    browser.get('http://www.baidu.com')
#openUrlBySeleniumWithFireFox()
#when the firefox cann't start,you should copy the 'geckodriver.exe' into the firefox install path like 'C:\Program Files\Mozilla Firefox'
#The second, you should put the firefox install path append to the system environment variable of 'PATH' ,don't forget input ';' for split PATH.
def getWebElementBySelenium():
    browser=webdriver.Firefox()
    browser.get('http://www.baidu.com')
    try:
        elem=browser.find_element_by_class_name('mnav')
        print('Found <%s> element with that class name'% (elem.tag_name))
    except:
        print('Was not able to find an element with that name.')
#getWebElementBySelenium()
def submitFormWithInputSend_keys():
    browser=webdriver.Firefox()
    browser.get('http://www.baidu.com')
    keyWordElem=browser.find_element_by_id('kw')
    keyWordElem.send_keys('Trump')
    buttonElem=browser.find_element_by_id('su')
    buttonElem.click()
#submitFormWithInputSend_keys()
from selenium.webdriver.common.keys import Keys
def sendKeysWithHomeAndEnd():
    browser=webdriver.Firefox()
    browser.get('http://www.qq.com')
    htmlElem=browser.find_element_by_tag_name('html')
    htmlElem.send_keys(Keys.END)
    htmlElem.send_keys(Keys.HOME)
    browser.back()
    browser.forward()
    browser.refresh()
    browser.quit()
#sendKeysWithHomeAndEnd()
import os,time
from selenium.webdriver.common.action_chains import ActionChains
def testIe():
    IEDriverServer = "C:\Program Files (x86)\Internet Explorer\IEDriverServer.exe"
    os.environ["webdriver.ie.driver"] = IEDriverServer
    browser=webdriver.Ie(IEDriverServer)

    #browser.get('http://192.168.205.33/default/abframe/auth/login.jsp')
    browser.get('http://localhost:8080/default/abframe/auth/login.jsp')
    keyWordElem=browser.find_element_by_id('username')
    keyWordElem.send_keys('lubosi')
    passElem=browser.find_element_by_id('password')
    #passElem.send_keys('1234')
    buttonElem=browser.find_element_by_id('btnlogin')
    buttonElem.click()
    time.sleep(2)
    browser.switch_to.frame('topFrame1')
    planElem=browser.find_element_by_id('962')
    planElem.click()
    browser.switch_to.parent_frame()
    browser.switch_to.frame('menuFrame')
    pElem = browser.find_element_by_xpath('html/body/div/ul/li[3]/div')
    pElem.click()
    pElem2 = browser.find_element_by_xpath('html/body/div/ul/li[3]/ul/li[1]/div')
    pElem2.click()
    browser.switch_to.parent_frame()
    browser.switch_to.frame('bodyFrame')
    browser.switch_to.frame('大区汇总大类资金计划')
    monthSe = browser.find_element_by_id('planMonth').find_elements_by_xpath('//span/span[1]')
    ActionChains(browser).move_to_element(monthSe).perform()
    #monthSe=browser.find_element_by_name('planMonth')
    #.find_element_by_id('planMonth').find_elements_by_xpath('/span/span/span')
    #monthSe.clear().send_keys('2017-09')
    time.sleep(1)
    monthSe.click()
    #searchEle=browser.find_element_by_xpath('html/body/div/div/table[2]/tbody/tr[2]/td/div/span')
    #searchEle.click()

testIe()