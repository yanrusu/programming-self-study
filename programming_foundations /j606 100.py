k,q,r=map(int,input().split())
a=[[0]*q for i in range(r)]*2
ain=list(input())
for i in range(0,r,1):
    for j in range(k):
        a[i][j] = ain[j]

for i in range(q):
    ain2=list(int,input().split())
    for i in range(1,r,1):
        for j in range(k):
            a[i][j]=ain[j]

