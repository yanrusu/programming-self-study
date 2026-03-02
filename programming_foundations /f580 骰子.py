n,m=map(int,input().split())
oa=[[1,3,4,5,2,6] for i in range(n)]
for i in range(m):
    a,b=map(int,input().split())
    if b==-1:
        #oa[a-1][0],oa[a-1][1],oa[a-1][2],oa[a-1][5]=oa[a-1][2],oa[a-1][0],oa[a-1][5],oa[a-1][1]
        oa[a-1][0],oa[a-1][1],oa[a-1][2],oa[a-1][5]=oa[a-1][1],oa[a-1][5],oa[a-1][0],oa[a-1][2]

    elif b==-2:
        #oa[a-1][0],oa[a-1][4],oa[a-1][3],oa[a-1][5]=oa[a-1][3],oa[a-1][0],oa[a-1][5],oa[a-1][4]
        oa[a-1][0],oa[a-1][3],oa[a-1][4],oa[a-1][5]=oa[a-1][3],oa[a-1][5],oa[a-1][0],oa[a-1][4]
    else:
        oa[a-1],oa[b-1]=oa[b-1],oa[a-1]

for i in range(0,n):
    print(oa[i][0],end=' ')
