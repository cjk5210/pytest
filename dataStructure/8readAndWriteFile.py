


# The path of test is 'E:\tensor\pytest\pytest\operateFile' or 'E:\tensor\pytest\pytest\testDef'

import os


def getCwd():
    cwd=os.getcwd()
    print(cwd)
    os.chdir('E:\\tensor\\pytest\\pytest\\operateFile')  # Change to another path
    cwd=os.getcwd()
    print(cwd)
#getCwd()

def mkdir():
    os.makedirs('e:\\mkdir')
#mkdir()

def someOperateAboutPath():
    print(os.path.abspath('.'))             #.or.\\is mean current path
    print(os.path.abspath('..\\..\\'))      #..\\is mean the uper path
    print(os.path.isabs(os.path.abspath('.'))) #judge a path is a absolute path or not
    print(os.path.relpath('c:\\Windows','c:\\')) #return the relative path from the second parameter to the first parameter
  #  print(os.path.relpath('c:\\Windows',os.getcwd()))
   # print(os.path.relpath('c:\\','d:\\'))
    print(os.path.relpath('E:\tensor\pytest\pytest\dataStructure', 'E:\tensor\pytest'))
    print(os.path.relpath( 'E:\tensor\pytest','E:\tensor\pytest\pytest\dataStructure'))

    print(os.path.basename('c:\\Window\\System32\\calc.exe'))#return the file name like calc.exe
    print(os.path.dirname('c:\\Windows\\System32\\calc.exe'))#return the file path like c:\Windows\System32\
    calcFilePaht='c:\\Windows\\System32\\calc.exe'
    print(os.path.split(calcFilePaht))#return a List include path at first and file name at second position
    print((os.path.dirname(calcFilePaht),os.path.basename(calcFilePaht)))#consctruct a Tuple with path and file name
    print(calcFilePaht.split(os.path.sep))
    print('/usr/bin'.split(os.path.sep))#this test should on the Centos system.

#someOperateAboutPath()

def checkAvailableOfTheFileAndPath():
    print('The path ','c:\\Windows is exists ',os.path.exists('c:\\Windows'),'.')
    print ('The path ','c:\\some_made_up_folder is exists ',os.path.exists('c:\\some_made_up_exists'),'.')
    print('The string ','c:\\Windows\\System32 is a path ',os.path.isdir('c:\\Windows\\System32'),'.')
    print('The string ','c:\\Windows\\System32\\calc.exe is a file',os.path.isfile('c:\\Windows\\System32\\calc.exe'),'.')
#checkAvailableOfTheFileAndPath()
def readOrWriteFile():
    helloFile=open('E:\\tensor\\pytest\\pytest\\testDef\\helloFile.txt','w')
    helloFile.write('hello world!\nhello world2!!!\n')
    helloFile.close()
    helloFile=open('e:\\tensor\\pytest\\pytest\\testDef\\helloFile.txt','r')
    alllines = helloFile.readlines()
    helloFile2=open('e:\\tensor\\pytest\\pytest\\testDef\\helloFile.txt','r').read()
    print('start : ',helloFile2)
    for line in alllines:
        print(line)
    helloFile.close()
    helloFile=open('e:\\tensor\\pytest\\pytest\\testDef\\helloFile.txt','a')
    helloFile.write('The second time of print \'hello world again!\'\n')
    helloFile.close()
    helloFile=open('e:\\tensor\\pytest\\pytest\\testDef\\helloFile.txt')#without the second parameter the default open mode is only read.
    alllines = helloFile.readlines()
    for line in alllines:
        print(line)
#readOrWriteFile()
import shelve
def saveThePropertyIntoAShelveFile(): #like save into a map,but it can save into a file for use when the system reboot
    shelfFile=shelve.open('e:\\tensor\\pytest\\pytest\\testDef\\shelveDateFile')
    cats=['Zophie','Pooka','Simon']
    shelfFile['cats']=cats
    print(type(shelfFile))
    print(shelfFile['cats'])
    print(list(shelfFile.keys()))#get the values by key is not a real list,we should transform the result into a list by the function 'list()'
    print(list(shelfFile.values()))
    shelfFile.close()
#saveThePropertyIntoAShelveFile()
import random
def shuffleListOrTuple():
    oneList=['1','2','3','4']
    oneLise1=['5','6','7','8']
    random.shuffle(oneList)
    random.shuffle(oneLise1)
    print(oneList)
    print(oneLise1)
shuffleListOrTuple()

