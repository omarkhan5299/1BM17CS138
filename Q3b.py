import string
import random

spch = ['/','%','$','@','*']

length = int(input("Enter the length of the pass:"))

lc = [random.choice(string.ascii_lowercase) for i in range(length)]

uc = [random.choice(string.ascii_uppercase) for i in range(length)]

sc = [random.choice(string.punctuation) for i in range(length)]

num = [random.choice(string.digits) for i in range(length)]

genpass = ''.join(sc+uc+lc+num)

genpass = ''.join(random.choice(genpass) for i in range(length))

print("Your generated password is:",genpass)
