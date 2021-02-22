sum=0
flag=1
n=(input("enter the number"))
length=len(n)
temp=int(n)
for i in n:
    z=int(i)
    sum=sum+(z**length)
if(sum==temp):
    print(temp,"its armstrong")
else:
    print(temp,"its not armstrong")
