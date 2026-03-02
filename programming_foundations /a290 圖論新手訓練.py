while True:
    
    n,m=map(int,input().split())
    road=[[]*m for _ in range(n)]
    for i in range(m):
        a,b=map(int,input().split())
        road[a-1].append(b-1)
        if i==m-1:
            if (b-1) in road[a-1]:
                print("Yes!!!")
            else :
                print("No!!!")
    
