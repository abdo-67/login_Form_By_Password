import time


count = 5
c = 5
truePassword = 0000

inputPassword = int(input("enter password "))

while inputPassword != truePassword:
    c = 5
    while c >= 1:
        count = 5
        if c ==5:
            while count > 1:
                print("password is wrong")
                count -= 1
                print(f" {'last one'.upper() if count ==1 else f'you have{count} tries' } ")
                print("\n")
                inputPassword = int(input("please enter true password".upper()))
                print("\n")
            else:
                print("\n")
                print('try remember your password,you can login after 15 sec')
                print("\n")
                time.sleep(15)
        else:
            inputPassword = int(input("enter password "))
            while count > 1:
                print("password is wrong")
                count -= 1
                print(f" {'last one'.upper()if count== 1  else f'you have anther {count} tries'}")
                print("\n")
                inputPassword = int(input("please enter true password ".upper()))
                print("\n")
            else:
                if c == 2:
                    print("\n")
                    print('be careful this is last chance,after this you can\'t login'.upper())
                    time.sleep(15)
                    print("\n")
                elif c== 1:
                    print("")
                else:
                    print("\n")
                    print('try remember your password,you can login after 15 sec')
                    time.sleep(15)
                    print("\n")
        c = c - 1   ######################################################
    else:
        print("sorry you can't login now".upper())
        break
else:
    print("login")
