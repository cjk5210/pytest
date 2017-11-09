import os,shutil
## The path of test is 'E:\tensor\pytest\pytest\testDef'
def copyFile():
    os.chdir('E:\\tensor\pytest\pytest\\testDef')
    path=shutil.copy('E:\\tensor\pytest\pytest\\testDef\helloFile.txt','E:\\tensor\pytest\pytest\\testDef\helloFileCopy.txt')
    print('net path at :',path)

#copyFile()
def copyFolder():
    os.chdir(' C:\\')
    shutil.copytree(' C:\\ bacon', 'C:\\ bacon_ backup')
#copyFolder()
def deleteFileOrFolder():
    os.unlink('path')#
    os.rmdir('path')#the folder of the path must be null
    shutil.rmtree('path')#the code can delete all of the file and folder include under the path
#deleteFileOrFolder()
import send2trash
def safeDeleteFileOrFolder():
    baconFile=open('E:\\tensor\pytest\pytest\\testDef\\bacon.txt','a')
    baconFile.write('Bacon is not a vegetable')
    baconFile.close()
    send2trash.send2trash('E:\\tensor\pytest\pytest\\testDef\\bacon.txt')
#safeDeleteFileOrFolder()


#I will finish off this error

def safeDeleteFileOrFolder2():
    baconFile=open('bacon.txt','a')
    baconFile.write('Bacon is not a vegetable')
    baconFile.close()
    send2trash.send2trash('bacon.txt')

#safeDeleteFileOrFolder2()
def walkForTraverseFolder():
    for folderName,subfolders,filenames in os.walk('C:\Windows\Logs'):
        print('The current folder is '+ folderName)
        for subfolder in subfolders:
            print('SUBFOLDER OF '+folderName+': '+subfolder)
        for filename in filenames:
            print('FILE INSIDE '+ folderName+': '+filename)
        print('')
#walkForTraverseFolder()
import traceback
def saveTheExceptionTracebackInfoIntoAFile():
    try:
        raise Exception('This is the error message.')
    except:
        errorFile=open('errorInfo.txt','w')
        errorFile.write(traceback.format_exc())
        errorFile.close()
        print('The traceback info was written to errorInfo.txt')
saveTheExceptionTracebackInfoIntoAFile()