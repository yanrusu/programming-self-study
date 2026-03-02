def dfs(x,y):
    global r,c,la
    m[x][y]=-1
    for tx,ty in [(0,1),(1,0),(0,-1),(-1,0)]:
        if x+tx>=0 and x+tx<r and y+ty>=0 and y+ty<c:
            if m[x+tx][y+ty]==la:
                dfs(x+tx,y+ty)
def sor(s):
    #return s[1]*256-ord(s[0])
    
    
    
    

        
w=int(input())
for _ in range(w):
    m=[];l={}
    r,c=map(int,input().split())
    for i in range(r):
        a=input()
        m.append(list(a))
    for i in range(r):
        for j in range(c):
            if m[i][j]!=-1:
                la=m[i][j]
                l[la]=l.get(la,0)+1
                dfs(i,j)

    l=sorted(l.items(),key=sor,reverse=True)
