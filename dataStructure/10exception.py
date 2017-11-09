import logging
logging.basicConfig( level= logging.DEBUG, format=' %(asctime) s - %(levelname) s - %(message) s')


"""
Traceback (most recent call last):
  File "E:/tensor/pytest/pytest/dataStructure/10exception.py", line 4, in <module>
    raiseAException()
  File "E:/tensor/pytest/pytest/dataStructure/10exception.py", line 3, in raiseAException
    raise Exception('This is the error message')
Exception: This is the error message

"""

def raiseAException():
    raise Exception('This is the error message')
#raiseAException()

def boxPrint(symbol,width,height):
    if len(symbol)!=1:
        raise Exception('Symbol must be a single character string.')
    if width <=2:
        raise Exception('Width must be greater than 2.')
    if height <=2:
        raise Exception('Height must be greater than 2.')
    print(symbol*width)
    for i in range(height-2):
        print(symbol+(' '*(width-2)) + symbol)
    print(symbol*width)
def testBoxPrint():#call the boxPrint() method
    for sym,w,h in (('*',4,4),('o',20,5),('x',1,3),('ZZ',3,3)):
        try:
            boxPrint(sym,w,h)
        except Exception as err:
            print('A exception happpended:'+str(err))
#testBoxPrint()
def spam():#call the bacon() method
    bacon()
# #traceback a exception and find the source code and the number which line occurred error
def bacon():#raise a exception
    raise Exception('This is the error message.')
#spam()
def catchTheException():
    try:
        spam()
    except Exception as err:
        print(str(err))
#catchTheException()
import traceback
def saveTheExceptionInfoIntoAFile():
    try:
        raise Exception(' This is the error message.')
    except:
        errorFile = open(' errorInfo. txt', 'w')
        errorFile. write( traceback.format_exc())
        errorFile. close()
        print(' The traceback info was written to errorInfo. txt.')
#saveTheExceptionInfoIntoAFile()

def assertForTest():
    podBayDoorStatus = 'open'
    assert podBayDoorStatus == 'open', 'The pod bay doors need to be "open".'
    podBayDoorStatus = 'I\' m sorry, Dave. I\' m afraid I can\'t do that.'
    assert podBayDoorStatus == 'open', 'The pod bay doors need to be "open".'
#assertForTest()


# 2017-11-08 15:17:39,789 - DEBUG - Some debugging details.
# 2017-11-08 15:17:39,789 - INFO - The logging module is working.
# 2017-11-08 15:17:39,789 - WARNING - An error message is about to be logged.
# 2017-11-08 15:17:39,789 - ERROR - An error has occurred.
# 2017-11-08 15:17:39,789 - CRITICAL - The program is unable to recover!

def testLogging():
    logging.debug('Some debugging details.')
    logging.info('The logging module is working.')
    logging.warning('An error message is about to be logged.')
    logging.error('An error has occurred.')
    logging.critical('The program is unable to recover!')
#testLogging()
def saveTheLoggingInfoIntoAFile():
    """
    need change the loggingConfig:
    import logging
    logging.basicConfig( filename='myProgramLog.txt', level= logging.DEBUG, format='%(asctime) s - %(levelname) s - %(message) s')
    :return:
    """
    print("import logging\nlogging.basicConfig( filename='myProgramLog.txt', level= logging.DEBUG, format='%(asctime) s - %(levelname) s - %(message) s')")
#saveTheLoggingInfoIntoAFile()