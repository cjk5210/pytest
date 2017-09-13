import random

#https://www.liaoxuefeng.com/
def testPrint():
    print('100+200=',100+200)
    print('100+200='+str(100+200))
#testPrint()
def testPrit1():
    print('Hello world!')
    print('What is your name?')
    myName=input()
    print('It is good to meet you, '+myName)
    print('The length of your name is:')
    print(len(myName))
    print('What is your age?')
    myAge=input()
    print('You will be '+ str(int(myAge)+1)+' in a year.')
#testPrit1()
def testWhile():
    name=''
    while name!='your name':
        print('Please type your name.')
        name=input()
    print('Thank you,',name)

#testWhile()
def testBreak():
    while True:
        print('Pleast type your name.')
        name=input()
        if name=='your name':
            break
    print('Thank you! ',name)

#testBreak()
def testContinue():
    while True:
        print('Who are you?')
        name=input()
        if name!='Joe':
            continue
        print('Hell,Joe,What is the password ?(It is a fish.)')
        password=input()
        if password=='swordfish':
            break
    print('Access granted.')

#testContinue()

def testForRange():
    print('My name is')
    for i in range(5):
        print('Jimmy Five Times('+str(i+1)+')')

#testForRange()
def testForRange2():
    for i in range(3):
        print(i)
# testForRange2()
# 0
# 1
# 2
def testRange():
    for i in range(5,11,2):
        print(i)
    print('------')
    for i in range(5, -1, -1):
        print(i)

#testRange()
# 5
# 7
# 9
# ------
# 5
# 4
# 3
# 2
# 1
# 0
#cjk
def testParameter():
    print('Hello',end=' ')
    print('World')
    print('cats','dogs','mice',sep=',')


#testParameter()
def guessGame():
    secretNumber=random.randint(1,20)
    print('I am thinking of a number between 1 and 20.')
    for guessesTaken in range(1,7):
        print('Take a guess.')
        guess=int(input())
        if guess<secretNumber:
            print('Your answer is too low.')
        elif guess>secretNumber:
            print('Your answer is too high.')
        else:
            break
    if guess==secretNumber:
        print('Good job! You guessed my number in '+str(guessesTaken)+' guesess')
    else:
        print('Nope.The number I was thinking of was '+ str(secretNumber))
guessGame()