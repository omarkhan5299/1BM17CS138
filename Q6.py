def mycheck(str1):
    list(str1)
    count = int(0)
    for el in str1:
        if el == '(':
            count+=1
        elif el == ')':
            count-=1
        elif el == '[':
            count+=2
        elif el == ']':
            count-=2
        elif el == '{':
            count+=3
        elif el == '}':
            count-=3
        else:
            pass

    if count == int(0):
            return 1
    else:
            return 0

mystr="([{}]"
print(mycheck(mystr))
