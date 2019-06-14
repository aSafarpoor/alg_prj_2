def main(n,s):
	list=[0 for i in range(2**n)]
	#print(list)
	ss=s+s
	if(len(s)==2**n):
		pass
	else:
		return 0
	p=2**n
	for i in range(len(s)):
		m=int(ss[i:i+n],2)
		#print(ss[i:i+n]," ",m)
		list[m]=1
	if(0 in list):
		return 0
	else:
		return 1

	
n=int(input())
s=input()	
print(main(n,s))
