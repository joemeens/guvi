str1=input()

if(len(str1)%2!=0):
    a=int(len(str1)/2)
    s1=str1[:a]
    s2=str1[a+1:len(str1)]
    str2=s1+"*"+s2
    print(str2)           #BASICS
if(len(str1)%2==0):
    a=int(len(str1)/2)
    s1=str1[:a-1]
    s2=str1[a+1:len(str1)]
    str3=s1+"**"+s2
    print(str3)
