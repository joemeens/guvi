number=list(map(int,input().split(" ")))
max1=0
if(len(number)==10):
    for i in number:
         if(i>max1):
                max1=i
print(max1)
  
