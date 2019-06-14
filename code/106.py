a1,a2=map(int,input().split())
bis=list(map(int,input().split()))
answer=[]
for i in bis:
    if i%2!=0:
        answer.append(i)
for i in range(1,len(answer)+1):
    if i==a2:
        print(answer[i-1])
