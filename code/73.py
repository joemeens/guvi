num1=int(input())
a,b=map(int,input().split(" "))
for i in range(a+1,b):
    if(num1==i):
        print("yes")
        break
else:
    print("no")
        
