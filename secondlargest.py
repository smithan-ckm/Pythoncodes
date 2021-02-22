n=int(input("Enter a number"))
list=[]
for i in range(0,n):
    a=int(input("enter a number"))
    list.append(a)
list.sort()
print(list[n-2])
