str = input("Enter the string to reverse:")

print("Original string:",str)

new_str = str.split(" ")
new_str=new_str[-1::-1]
final=' '.join(new_str)
print("Reversed String 1:",final)

str1 = str.split(" ")
ans=[]
for x in str1:
    ans.append(x[::-1])
    



finalans = ' '.join(ans)
print("Reversed String 2:",finalans)
