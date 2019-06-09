ren=input()
count=0
for er in ren:
    if(er.isalpha()==True):
        continue
    elif(er.isdigit()==True):
        continue
    elif(er==" "):
        continue
    else:
        count=count+1
print(count)
