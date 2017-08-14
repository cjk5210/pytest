n = 0
while n<3:
    user=raw_input('please enter your name:')
    password=raw_input('passwd:')
    if user == 'buer' and password == '1234.com':
        print('login successful!')
        while True:
            shu = raw_input('>>>:')
            if shu == 'quit':
                n=3
                break
    else:
        print('login fail')
        n+=1