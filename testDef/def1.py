import math

def fahrenheit_converter(C):
    fahrenheit=C*9/5+32
    print(fahrenheit)
#print(fahrenheit_converter(100))

#print(fahrenheit_converter(35))

def convertToKG(g):
    return str(g/1000)+'kg'
#print(convertToKG(5000))

def sanJiao(x,y):
    return math.sqrt(x*x+y*y)
#print(sanJiao(3,4))
#print(sanJiao(x=4,y=3))

def text_create(name,msg):
    f_path='c://pythontest/pytest/pytest/testDef/'
    full_path=f_path+name+'.txt'
    file=open(full_path,'w')
    file.write(msg)
    file.close()
    print('Done')
#text_create('helloPython','hello world')

def test_filter(word,censored_word='lame',changed_word='Awesome'):
    print(word.replace(censored_word,changed_word))
    return word.replace(censored_word,changed_word)
#test_filter('Python is lame!')
def jia(a,b):
    print(a+b)
    return a+b
def jian(a,b):
    print(a-b)
    return a-b
def cheng(a,b):
    print(a*b)
    return a*b
def chu(a,b):
    if b==None or b==0:
        print('ERROR!!! The number 0 cann\'t be The bei chu number!!! ')
        return 'ERROR!!!'
    elif a==0:
        print('0')
        return 0
    else:
        print(a/b)
        return a/b
# print(chu(8,0))

def testLoop():
    for every_letter in 'Hello World!':
        print(every_letter)

# testLoop()
def testLoopNumJia(num):
    for i in range(0,num):
        print(str(i)+' + 1 =',i+1,' ',str(i),' * 2 = ',i*2)

#testLoopNumJia(99)
def testChengFaKouJue():
    for i in range(1,10):
        for j in range(1,i+1):
            print('{} X {} = {}'.format(i,j,i*j),end='    ')
        print()
#testChengFaKouJue()

def testWhile(num):
    count =0
    while True:

        count=count+1
        print('Repeat this Line !'+str(count))
        if count==num:
            break
#testWhile(40)
def printOuShu():
    num=2
    while True:
        if(num<=100):
            print(num)
            num=num+2
        else:
            print('over!!!')
            break
#printOuShu()
import random
def roll_dice(numbers=3,points=None):
    print('<<<<< ROLL THE　DICE! >>>>>')
    if points is None:
        points=[]
    while numbers>0:
        point=random.randrange(1,7)
        points.append(point)
        numbers=numbers-1
    return points
def roll_result(total):
    isBig=11<=total<=18
    isSmall=3<=total<=10
    if isBig:
        return 'Big'
    elif isSmall:
        return 'Small'
def start_game():
    print('<<<<< GAME STARTS! >>>>> ')
    choices=['Big','Small']
    your_choice=input('Big Small :')
    if your_choice in choices:
        points=roll_dice()
        total=sum(points)
        youWin=your_choice==roll_result(total)
        if youWin:
            print('The points are',points,'You Win!!!')
        else:
            print('The points are',points,'You Lose!!!')
    else:
        print('Invalid Words')
        start_game()
#start_game()
