cont=int(input())
if(cont>1):
    for i in range(2,cont):
        if(cont%i==0):
            print("no")
            break
    else:
        print("yes")
