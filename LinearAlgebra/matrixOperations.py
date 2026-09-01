row=int(input("Enter Number of rows for matrix M."))
column=int(input("Enter Number of columns for matrix M."))

# matrix
M=[]

# Input matrix elements
for i in range(row):
    temp=[]
    for j in range(column):
        element=int(input(f"Enter element for {i+1} and {j+1} place."))
        temp.append(element)
    M.append(temp)
print("Matrix : ",M)

# single value print
for rows in M:
    for col in rows:
        print(f"Element {col} ",end="")
    print()

# rows display
for i in range(row):
    print(f"Row {i+1} : {M[i]}")
    
# columns display

for j in range(column):
    c=[]
    for i in range(row):
        c.append(M[i][j])
    print(f"Column {j+1} : {c}")
    
sc=[]
# scalar input
scalar=int(input("Enter Scalar value."))
for i in range(row):
    temp=[]
    for j in range(column):
        s=M[i][j]*scalar
        temp.append(s)
    sc.append(temp)
print("Scalar Multiplication.",sc)
        
# transpose matrix
t=[]
for j in range(column):
    temp=[]
    for i in range(row):
        temp.append(M[i][j])
    t.append(temp)
print("Transpose of matrix M.",t)
