arr=[]
lst=[]
n=int(input("Enter the number of elements in the list"))
for i in range(0,n):
    ele=int(input())
    arr.append(ele)
print("User entered list:")
print(arr)
for i in arr:
    if i%2==0:
        lst.append(i)
print("New list with even numbers:")
print(lst)

