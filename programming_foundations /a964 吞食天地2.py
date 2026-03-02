while True:
    try:
        n,m=map(int,input().split())
        a=[[]]
        for i in range(n):
            a.append([int(x) for x in input().split()])

        for _ in range(m):
            sum_=0
            p=[int(x) for x in input().split()]
            for i in range(p[2]):
                for j in range(p[3]):
                    sum_+=a[i][j]
            print(sum_)
        
    except:break
