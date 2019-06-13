row=5
total=row*row
black="black"

def inintial():
	global row,total
	node_list={}
	bool_list = []
	
	arr=[]
	for i in range(row):
		sub_arr=[]
		for j in range(row):
			sub_arr.append([])
		arr.append(sub_arr)
		
	for i in range(total):
		new_in=input()[1:-1].split(",")
		node_list[i]=new_in
		bool_list.append(False)
	return node_list, bool_list,arr

def check(x,y,bool_list,i):
	#(up,left,down,right).
	up=0
	left=1
	down=2
	right=3
	
	global arr,node_list,row,total,black
	node=node_list[i]
	if(x==up):
		if(not node[up]==black):
			return False
	else:
		up_node_code=arr[x-1][y]
		up_node=node_list[up_node_code]
		if(not up_node[down]==node[up]):
			return False
	
	if(x==row-1):
		if(not node[down]==black):
			return False
			
	if(y==0):
		if(not node[left]==black):
			return False
	else:
		left_node_code=arr[x][y-1]
		left_node=node_list[left_node_code]
		if(not left_node[right]==node[left]):
			return False
		
	if(y==row-1):
		if(not node[right]==black):
			return False

	return True
			
def init_map(num,bool_list):
	global total
	global row
	global arr
	global node_list
		
	if (num>=total):
		return True
	x=int(num/row)
	y=int(num%row)
	
	for i in range(total):
		if(bool_list[i]==False):
			status=check(x,y,bool_list,i)
			if (status==True):
				bool_list[i]=True
				arr[x][y]=i
				return(init_map(num+1,bool_list)) 
	return False



node_list,bool_list,arr=inintial()
#print(node_list)
#print(bool_list)
#print(arr)
final_status=init_map(0,bool_list)
#print(final_status)
#print('')

if(final_status):
	for i in  range(row):
		for j in range(row):
			print ("(",end="")
			for k in range(len(node_list[arr[i][j]])):
				print (node_list[arr[i][j]][k],end="")
				if(k<3):
					print(",",end="")
			print (")",end="")
			if(j<row-1):
				print(";",end="")
			
			
		if(i<row-1):
				print('')
				



