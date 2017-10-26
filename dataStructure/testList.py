def testFor():
    for takes in range(1,10):
        print('takes',takes)
    print('globle takes=',takes)
#takes is a global variable,not including the for loop

#testFor()
import random
def shuffleListOrTuple():
    oneList=['1','2','3','4']
    oneLise1=['5','6','7','8']
    random.shuffle(oneList)
    random.shuffle(oneLise1)
    print(oneList)
    print(oneLise1)
shuffleListOrTuple()