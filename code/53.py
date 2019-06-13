digit1=int(input())
sum=0
while(digit1>0):
    rem=digit1%10
    sum=sum+rem
    digit1=digit1//10
print(sum)
