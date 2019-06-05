los=input()
los=int(los)
digit=0
temp=los

while(temp<0):
    rem=temp%10
    digit=digit+(rem**3)
    temp=temp//10


if(los==digit):
    print("yes")
else:
    print("no")
