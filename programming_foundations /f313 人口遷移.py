r,c,k,m=map(int,input().split())
rc=[]
for i in range(r):
    rc.append([int(x) for x in input().split()])
for i in range(m):
    rc1=[[0]*c for i in range(r)]
    for i in range(r):
        for j in range(c):
            if rc[i][j]!=-1:
                if i>0:
                    if rc[i-1][j]!=-1:
                        rc1[i-1][j]+=rc[i][j]//k
                        rc1[i][j]-=rc[i][j]//k
                        



                if i<(r-1):
                    if rc[i+1][j]!=-1:
                        rc1[i+1][j]+=rc[i][j]//k
                        rc1[i][j]-=rc[i][j]//k
                


                if j>0:
                    if rc[i][j-1]!=-1:
                        rc1[i][j-1]+=rc[i][j]//k
                        rc1[i][j]-=rc[i][j]//k


                if j<(c-1):
                    if rc[i][j+1]!=-1:
                        rc1[i][j+1]+=rc[i][j]//k
                        rc1[i][j]-=rc[i][j]//k
    for i in range(r):
        for j in range(c):
            rc[i][j]+=rc1[i][j]
maxmin=[]
for i in range(r):
    q=rc[i].count(-1)
    for j in range(q):
        rc[i].remove(-1)
    maxmin.append(max(rc[i]))
    maxmin.append(min(rc[i]))

print(min(maxmin))
print(max(maxmin))
    
