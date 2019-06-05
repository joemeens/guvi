low,up=input().split()
low=int(low)
up=int(up)
for i in range(low,up+1):
    if(i>1):
        for j in range(2,i):
            if(i%j==0):
                break
        else:
            print(i)
