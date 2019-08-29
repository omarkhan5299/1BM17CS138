def check_el(arr,search):
    if search in arr:
        return 1
    else:
        return 0


arr=[]
n=int(input("Enter the size of the array:"))
for i in range(0,n):
    el=int(input("Enter the element:"))
    arr.append(el)

    
search= int(input("Enter the element to search for:"))

if(check_el(arr,search)):
    print("Yes,",search,"is present!")
else:
    print("No,",search,"is not present!")
          




