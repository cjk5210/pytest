import subprocess
def openOtherProgram():
    calcProc=subprocess.Popen('c:\\Windows\\System32\\calc.exe')
    print('1',calcProc.poll()==None)
    print('2',calcProc.wait())
    print('3',calcProc.poll() == None)
openOtherProgram()
