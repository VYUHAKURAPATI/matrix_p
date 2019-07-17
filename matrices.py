#transpose of a matrix
#for loop for the list
#for loop for the index in a list 
#exchange the index
 


#?
def transpose_matrix(mat1):
	result=[]
	for i in range(len(mat1)):
		row=[]
		for j in range(len(mat1[i])):
			row.append(mat1[j][i])
			
		result.append(row)
	return result 
	

		

#?
#add two matrix a and b

def sum_matrix(a,b):	
	big_list=[]
	for i in range(len(a)):
		row=[]
		
		for j in range(len(a[i])):
			row.append(a[i][j]+b[i][j])
		
		big_list.append(row)
	return big_list
	
#another way
def sum_matrix1(a,b):
	for i in range(len(a)):
		for j in range(len(a[i])):
			a[i][j]=a[i][j]+b[i][j]
	return a

		
def matix_multiplication(a,b):
	pass
	
	
def determinant_matrix(a):
	pass 
	
def inverse_matrix(a):
	pass 
	
	
			
	