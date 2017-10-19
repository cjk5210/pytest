


# The path of test is 'E:\tensor\pytest\pytest\operateFile'

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
    pass