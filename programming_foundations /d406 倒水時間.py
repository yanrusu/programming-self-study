nt=0
try:
    while True:
        nt+=1
        s=int(input())
        n,m=map(int,input().split())
        w=[[0]*(m+2)]
        for _ in range(n):
            w.append([0]+[int(x) for x in input().split()]+[0])
            if _==0:
                c1=w[1].index(1) 
    
        w.append([0]*(m+2))
        
        q1=[];q2=[[1,c1]]
        t=0
        while True:
            if not q1:        #如果q1空了
                t+=1
                q1,q2=q2,q1   #交換
            if q1==q2:break   #如果兩個q相等，代表兩個都是零 
            r,c=q1[0][0],q1[0][1]
            if w[r+1][c]==1:
                q2.append([r+1,c])
                w[r+1][c]+=t
                if r==1 and c1==c :
                    w[r][c1]=0 #第一個定是1避免與判斷衝突，所以先設為其他數，輸出時再重賦值
            if w[r-1][c]==1:
                if s==1:    #S=1才能往上走
                    q2.append([r-1,c])
                    w[r-1][c]+=t
                    if r==1 and c1==c :
                        w[r][c1]=0

            if w[r][c+1]==1:
                q2.append([r,c+1])
                w[r][c+1]+=t
            if w[r][c-1]==1:
                q2.append([r,c-1])
                w[r][c-1]+=t
            del q1[0]
        w[1][c1]=1
        w.pop(0);w.pop();w[0].pop();w[0].pop(0) #將外面那圈刪除（好像偏麻煩
        print(f'Case {nt}:')
        for i in range(len(w)):
            if i!=0:
                w[i].pop()
                w[i].pop(0)
                i!=0
                a=w[i].count(1)
                for z in range(a):
                    j=w[i].index(1)
                    w[i][j]=0
            print(*w[i])
except:pass
