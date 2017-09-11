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


