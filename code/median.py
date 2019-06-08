#median element of an array
num1=int(input())
a=list(map(eval,input().split(" ")))
b=sorted(a)
length=len(a)
if(len(b)%2!=0):
    print(b[len(b)//2])
else:
    c=(b[(length)//2]+b[(length)//2-1])/2
    print(c)
    #2 3 4 5 4 6
    
