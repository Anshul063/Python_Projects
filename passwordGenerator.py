import random
import string

def generate_password():

    number_of_pw = int(input("Enter number of passwords"))

    length_of_pw = int(input("Enter length of passwords"))

    list = []

    for i in range(0,number_of_pw):
        str = string.ascii_letters + string.digits

        r = ''.join(random.choice(str) for j in range(length_of_pw))

        if r not in list:
            list.append(r)
            
    print(list)

generate_password()