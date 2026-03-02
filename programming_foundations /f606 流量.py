n,m,k=map(int,input().split())
s=[]
mi=float('inf')
for i in range(n):
    s.append([int(x) for x in input().split()])

for i in range(k):
    tot=0
    ctc=[[0]*m for i in range(m)]
    case=[int(x) for x in input().split()]
    for i in range(n):
        for j in range(m):
            ctc[case[i]][j]+=s[i][j]
    for i in range(m):
        for j in range(m):
            if i==j:
                tot+=ctc[i][j]*1
        
            elif ctc[i][j]<=1000:
                    tot+=ctc[i][j]*3

            else:
                tot+=ctc[i][j]*2+1000
    if tot!=0:
        mi=min(tot,mi)
print(mi)
    
