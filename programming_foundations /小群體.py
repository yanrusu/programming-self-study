n=int(input())
fn=[int(x) for x in input().split()]
visit=[False]*n
g=0
for i in range(len(fn)):
    if visit[i]==True: continue
    a=fn[i]#4
    visit[i]=True
    p=i#0
    g+=1
    while a!=p:
        visit[a]=True
        a=fn[a]
    
print(g)
    
