str1=input()
l=["a","e","i","o","u","A","E""I","O","U"]
for i in range(0,len(str1)):
    if(str1[i] in l):
        print("yes")
        break
else:
    print("no")
