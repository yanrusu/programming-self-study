def dfs(i,j):
    global oil
    oil[i][j]='*'
    for i1,j1 in [[1,0],[0,1],[-1,0],[0,-1],[1,1],[-1,1],[-1,-1],[1,-1]]:
        if i1+i>=0 and j1+j>=0 and i1+i<r and j1+j<c and oil[i+i1][j+j1]=="@":
            dfs(i+i1,j+j1)





while True:
    oils=0
    r,c=map(int,input().split())
    if r+c==0: break
    oil=[]
    for _ in range(r):
        oil.append(list(input()))
    for r1 in range(r):
        for c1 in range(c):
            if oil[r1][c1]=="@":
                dfs(r1,c1)
                oils+=1
    print(oils)
            
        
    
    
