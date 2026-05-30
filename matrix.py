# Matrix Creation
rows=3
cols=3
mat=[]
for i in range(rows):
  row=[]
  for j in range(cols):
    num=int(input())
    row.append(num)
  mat.append(row)
print(mat)

# Sum of all numbers in a Matrix
A=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
total=0
for i in range(len(A)):
  for j in range(len(A[0])):
    total+=A[i][j]
print(total)

# Sum of two matrix
A=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
B=[[2, 0, 3], [6, 9, 1], [5, 2, 8]]
o=[]
for i in range(len(A)):
  res=[]
  for j in range(len(A[0])):
    res.append(A[i][j]+B[i][j])
  o.append(res)
print(o)
    
# Subtraction
A=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
B=[[2, 0, 3], [6, 9, 1], [5, 2, 8]]
o=[]
for i in range(len(A)):
  res=[]
  for j in range(len(A[0])):
    res.append(A[i][j]-B[i][j])
  o.append(res)
print(o)
    

