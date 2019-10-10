primez = open("primeno.txt","w")
for num in range(2,1001):
 
   if num > 1:
       for i in range(2,num):
           if (num % i) == 0:
               break
       else:
           #print(num)
           primez.write(str(num))
           primez.write("\n")

primez.close()
primez = open("primeno.txt","r")

#########################

happy_numbers = []
sqdict = {str(i):i**2 for i in range(10)}
def adder3(num):
    return sum(sqdict[i] for i in str(num))

def happynum(num,counter):
    i_sum = adder3(num)
    if i_sum == 1:
        happy_numbers.append(number)

        return 1
    else:
        counter+=1
        if counter > 50:
            return False
        else:
            happynum(i_sum,counter)
counter = 0
for i in range(0,1000):
    number = i
    happynum(number,counter)
happyz = open("happyno.txt","w")
for i in happy_numbers:
    happyz.write(str(i)+"\n")

happyz.close()
happyz = open("happyno.txt","r")
contents_p = primez.read()
new_p =[]
new_p = contents_p.split("\n")
contents_h = happyz.read()
new_h = []
new_h = contents_h.split("\n")


for i in new_p:
    for j in new_h:
        if i==j:
            print(i)
            break
        

    
        

    


        
