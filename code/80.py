#print the odd digits in the number
number1=input()
for i in number1:
    if(int(i)%2==0):
        continue
    else:
        print(i,end=" ")
