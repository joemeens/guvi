hs=input()
b=0
for j in hs:
	if(j=='1' or j=='0'):
		b=b+1
if(b==len(hs)):
	print("yes")
else:
	print("no")
