ext=int(input())
def word(s):
        s=list(s)
        return s

for i in range(ext):
    n,m,sr,sc,fr,fc=map(int,input().split())
    oa=[[1]*(m+2)]
    for i in range(n):
        x=input()
        oa.append([1]+word(x)+[1])
    oa.append([1]*(m+2))
    for i in range(n+1):
        for j in range(m+1):
            oa[i][j]=int(oa[i][j])
    q2=[[sr,sc]]
    q1=[]
    step=0
    p=False
    while q2:
        step+=1
        q1,q2=q2,q1
        if p :break
        while q1:
            r=q1[0][0];c=q1[0][1]
            if r==fr and c==fc:
                print(step)
                p=True
                break
            if oa[r+1][c]==0: q2.append([r+1,c])
            if oa[r-1][c]==0: q2.append([r-1,c])
            if oa[r][c+1]==0: q2.append([r,c+1])
            if oa[r][c-1]==0: q2.append([r,c-1])
            oa[r][c]=1
            del q1[0]

    if not p:
        print('0')
        
        
        

