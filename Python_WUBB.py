'''
Julian Vu
Guess it I guess
'''

import time
import os

pass_inp = 0

def pass_check(pass_inp):
    pass_inp = input("Please enter your 6-digit numeral password: ")
    too_much = 0
    '''
    password_inp = [pass_inp]
    print(password_inp)
    '''
    #input_pass = list(map(list, str(password_inp[0])))
    input_pass = [int(num) for num in str(pass_inp)]
    print(f"The password is {input_pass}")

    if len(input_pass) > 6 :
        too_much = len(input_pass) - 6
        print(f"You have {too_much} digit/digits extra.")
        print("Please make a 6-digit numeral password!")
        re_run()
    elif len(input_pass) < 6:
        too_much = 6 - len(input_pass)
        print(f"You need {too_much} digit/digits")
        print("Please make a 6-digit numeral password!")
        re_run()
    else:
        print("Your password is valid!")
        return pass_inp
        return password_inp
        return input_pass


def reset():
    wait_time = 5
    print(f"You will be able to retry in {wait_time} seconds!")
    for i in range(0, wait_time):
        time.sleep(1)
        os.system('close')
        print(f"You will be reset in {wait_time - i - 1} seconds!")
    os.system('close')

def re_run():
    while True:
        while True:
            again = input("Do you want to retry? (y/n): ")
            if again != "y" or again !=  "n":
                break
            print("Your input is invalid! Please retry.")
        if again == 'y':
            pass_check(pass_inp)
            break
        elif again == 'n':
            print("Goodbye.")
            break



pass_check(pass_inp)