time=int(input())
hrs=time//60
if(time<60):
    mins=time
else:
    mins=time%60
print(str(hrs) +" " + str(mins))
