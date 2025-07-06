import string
import random

def generate_password(min_len, num=True, special_char=True):#generate_password(10, False) # false mane length 10 thakbe use only special char krte parbe. 
    letter = string.ascii_letters
    digit = string.digits
    special = string.punctuation

    character = letter
    if num:
        character += digit
    if special_char:
        character += special

    pwd =""
    meet_criteria = False
    has_num = False
    has_special = False

    while not meet_criteria or len(pwd) < min_len:
        new_char = random.choice(character)
        pwd += new_char

        if new_char in digit:
            has_num =True
        elif new_char in special:
            has_special = True

        meet_criteria = True
        if num:
            meet_criteria  = has_num
        if special_char:
            meet_criteria = meet_criteria and has_special
    return pwd
        

   # print(letter, digit,special) #abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ 0123456789 !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
min_len = int(input("enter min lenght:"))
has_num = input("wnat number? (y/n) :").lower() == "y"
has_special = input("do u want special char? (y/n):").lower() == "y" 

pwd = generate_password(min_len, has_num, has_special)
print("password:", pwd)