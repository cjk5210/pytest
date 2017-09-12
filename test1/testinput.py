n = 0
while n<3:
    user=input('please enter your name:')
    password=input('passwd:')
    if user == 'buer' and password == '1234.com':
        print('login successful!')
        while True:
            shu = input('>>>:')
            if shu == 'quit':
                n=3
                break
    else:
        print('login fail')
        n+=1