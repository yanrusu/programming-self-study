m,n,h = map(int,input().split())
# 空0 木頭4 水平線 1 垂直 2 交叉 3
oa=[[0]*n for i in range(m)]
oa1a=[]
def addw(r,c):
    sc=False
    global oa,m,n
    oa[r][c]=4
    for i in range(r-1,-1,-1):
        if oa[i][c]==4:
            sc=True
            i1=i
            
        if sc:
            for i in range(r-1,i,-1):
                if oa[i][c]<4:
                    if oa[i][c]==1:oa[i][c]+=2
            
                    elif oa[i][c]==0:oa[i][c]+=2
            sc=False
        

    for i in range(r+1,m):
        if oa[i][c]==4:
            sc=True
            i1=i
        if sc:
            for i in range(r+1,i):
                if oa[i][c]<4:
                    if oa[i][c]==1:oa[i][c]+=2
                    elif oa[i][c]==0:oa[i][c]+=2
            sc=False

    for i in range(c+1,n):
        if oa[r][i]==4:
            sc=True
            i1=i
        if sc:
            for i in range(c+1,i):
                if oa[r][i]<4:
                    if oa[r][i]==2:oa[r][i]+=1
                    elif oa[r][i]==0 :oa[r][i]+=1
            sc=False

    for i in range(c-1,-1,-1):
        if oa[r][i]==4:
            sc=True
            i1=i
        if sc:
            for i in range(c-1,i,-1):
                if oa[r][i]<4:
                    if oa[r][i]==2:oa[r][i]+=1
                    elif oa[r][i]==0:oa[r][i]+=1
            sc=False



def removew(r,c):
    global oa,m,n
    oa[r][c]=0
    for i in range(r-1,-1,-1):
        if oa[i][c]==4:break
        elif oa[i][c]<4 :oa[i][c]-=2
    for i in range(r+1,m):
        if oa[i][c]==4:break
        elif oa[i][c]<4 :oa[i][c]-=2

    for i in range(c+1,n):
        if oa[r][i]==4:break
        elif oa[r][i]<4 :oa[r][i]-=1

    for i in range(c-1,-1,-1):
        if oa[r][i]==4:break
        elif oa[r][i]<4 :oa[r][i]-=1
for x in range(h):
    r,c,t=map(int,input().split())
    n1=0
    oa1=0
    if t==0:
        addw(r,c)
    else :
        removew(r,c)

    for i in range(m):
        oa1+=n-oa[i].count(0)
        n1+=n-oa[i].count(0)
    oa1a.append(oa1)
    print(oa)
print(max(oa1a))
print(n1)
    
