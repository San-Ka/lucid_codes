password = True
attempt = 0
while attempt < 3:
    password = print(input('What is the password?'))
    attempt = attempt +1
    if password == 'lucidcode':
     break
    if password == 'lucidcode':
        print('Yes, the password is ' + password.upper() + '. You may enter.')
    elif password == 'quite':
         Password = False
         print('OVER')
    else:
        print('Password does not match! please try again')
        
    
    
