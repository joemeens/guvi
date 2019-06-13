num1=input().split()
a1=list(map(int,input().split()))
a2=sorted(a1)
for i in range(0,len(a2)):
    print(a2[i],end=" ")
