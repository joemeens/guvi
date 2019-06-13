a,b=input().split()
a=int(a)
b=int(b)
l=list(map(int,input().split()))
count=0
for i in l:
    if(i==b):
        count+=1
    else:
        continue
if(count!=0):
    print("yes")
else:
    print("no")
