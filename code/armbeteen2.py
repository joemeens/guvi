p,q=input().split()
p=int(p)
q=int(q)
for i in range(p,q+1):
    od=len(str(i))
    digit=0
    temp=i
    while(temp>0):
        rem=temp%10
        digit=digit+(rem**od)
        temp=temp//10
    if(i==digit):
        print(i)
