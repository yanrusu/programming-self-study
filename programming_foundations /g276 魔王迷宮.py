n,m,k=map(int,input().split())
r=[]
b=[[0]*m for i in range(n)]
for i in range(k):
    a=[int(x) for x in input().split()]
    r+=[a]
while len(r)!=0:
    nr=[]

    for i in range(len(r)):
        e=r[i][0]
        q=r[i][1]
        if b[e][q]!=0: b[e][q]=-1
        else :nr.append(r[i])

    for z in range(n):
        for i in range(m):
            if b[z][i]==-1:
                b[z][i]=0
    r=[]          
    for i in range(len(nr)):
        sa=nr[i][0]
        ai=nr[i][1]
        b[sa][ai]=1
        nr[i][0]+=nr[i][2]
        nr[i][1]+=nr[i][3]
        if 0<=nr[i][0]<n and 0<=nr[i][1]<m:
            r.append(nr[i])

print(sum(b[i][j] for i in range(n) for j in range(m)))
            
            
        
                
                
                
        
        
    
        

