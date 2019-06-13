post=input()
x=0
for i in range(0,len(post)):
    if post[i].isdigit():
        x=x+1
        break
for i in range(0,len(post)):
      if post[i].isalpha():
        x=x+1
        break
if x==2:
      print("Yes")
else:
      print("No")
  
