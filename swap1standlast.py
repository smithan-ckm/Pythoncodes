n=int(input("Enter a number"))
list=[]
for i in range(0,n):
    a=int(input("enter a number"))
    list.append(a)
print(list)
temp=list[0]
list[0]=list[n-1]
list[n-1]=temp
print(list)
