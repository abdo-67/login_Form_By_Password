import time

tries1 = 5           # for small loop
tries2 = 5           # for big while loop

truePassword = 0000  # for example
inputPassword = int(input("enter password "))

while inputPassword != truePassword:
    tries2 = 5
    while tries2 >= 1:
        tries1 = 5
        if tries2 == 5:
            while tries1 > 1:
                print("password is wrong")
                tries1 -= 1
                print(f" {'last one'.upper() if tries1 ==1 else f'you have{tries1} tries' } ")
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
            while tries1 > 1:
                print("password is wrong")
                tries1 -= 1
                print(f" {'last one'.upper()if tries1== 1  else f'you have anther {tries1} tries'}")
                print("\n")
                inputPassword = int(input("please enter true password ".upper()))
                print("\n")
            else:
                if tries2 == 2:
                    print("\n")
                    print('be careful this is last chance,after this you can\'t login'.upper())
                    time.sleep(15)
                    print("\n")
                elif tries2 == 1:
                    print("")
                else:
                    print("\n")
                    print('try remember your password,you can login after 15 sec')
                    time.sleep(15)
                    print("\n")
        tries2 = tries2 - 1   # please don't forget this...
    else:
        print("sorry you can't login now".upper())
        break
else:
    print("login")
