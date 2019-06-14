nun=int(input())
a=list(map(int,input().split()))
list1=[]
for i in range(1,nun+1):
    list1.append(i)
for i in range(0,len(list1)):
    if a[i]!=list1[i]:
        print(i)
        break
