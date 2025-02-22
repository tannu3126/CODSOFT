import random
import string

def gen_pass(lenght):
    characters=string.ascii_letters+string.digits+string.punctuation
    password=''.join(random.choice(characters)for _ in range(lenght))
    return password
try:
    lenght=int(input("Enter the length="))
    if lenght<8:
        print("Password must be at least 8.")
    else:
        password= gen_pass(lenght)
        print("Password Generated",password)
except ValueError:
    print("Enter a valid number")