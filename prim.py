n=int(input())
e=0
if n>1:
	for i in range(2,n):
		if n%i==0:
			e=1
			break
	if e==0:
		print("yes")
	else:
		print("no")
