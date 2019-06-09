string=input()
count=1
for i in string:
    if(i=="." or i=="\n"):
        count=count+1
print(count)
