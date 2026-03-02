while True:
    try:
        r,c=map(int,input().split())
        oa=[[0]*r for i in range(c)]
        a=[]
        for z in range(r):
            a.append([int(x) for x in input().split()])



        for i in range(r):
            for j in range(c):
                oa[j][i]=a[i][j]

        for i in range(c):
            print(*oa[i])
    except:break
          
    
    
    
    
