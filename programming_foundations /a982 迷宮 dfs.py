def run(i,j):
    global p
    
    if p[i+1][j]>p[i][j]+1 and p[i+1][j]!=-1:
        p[i+1][j]=p[i][j]+1
        run(i+1,j)
        
    if p[i][j+1]>p[i][j]+1 and p[i][j+1]!=-1:
        p[i][j+1]=p[i][j]+1
        run(i,j+1)
        
    if p[i-1][j]>p[i][j]+1 and p[i-1][j]!=-1:
        p[i-1][j]=p[i][j]+1
        run(i-1,j)
        
    if p[i][j-1]>p[i][j]+1 and p[i][j-1]!=-1:
        p[i][j-1]=p[i][j]+1
        run(i,j-1)
        


n=int(input())
p=[]
for i in range(n):
    w=list(input())
    p.append(w)

    
for i in range(n):
    for j in range(n):
        if p[i][j]=="#": p[i][j]=-1
        else : p[i][j]=float("inf")
p[1][1]=1
run(1,1)

if p[n-2][n-2]==float("inf"): print("No solution!")
else :print(p[n-2][n-2])
