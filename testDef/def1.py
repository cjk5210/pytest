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
print(sanJiao(3,4))
