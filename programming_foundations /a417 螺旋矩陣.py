while True:
    try:
        for i in range(int(input())):
            s,d=map(int,input().split())
            sp=[[0]*s for _ in range(s)];rum=s-1;start=[0,0];num=1;time=0;true=False
            if d==1:
                for i in range(s):
                    sp[0][i]='   '+str(num)
                    num+=1
                    start[1]=i
                d=[[0,1],[1,0],[0,-1],[-1,0]]
                while True:
                    for i in range(2):
                        d=d[1:]+d[:1]
                        if time:
                            if time%2==0:
                            
                                rum-=1
                                if rum==0:
                                    true=True
                                    break
                        time+=1
                            
                        for j in range(rum):
                            start=[start[0]+d[0][0],start[1]+d[0][1]]
                            sp[start[0]][start[1]]='   '+str(num)
                            
                            num+=1
                    if true :break
        
                for i2 in range(s):
                    print(*sp[i2])

            else:

                for i in range(s):
                        sp[i][0]='    '+str(num)
                        num+=1
                        start[0]=i
                d=[[1,0],[0,1],[-1,0],[0,-1]]
                while True:
                    for i in range(2):
                        d=d[1:]+d[:1]
                        if time:
                            if time%2==0:
                                rum-=1
                                if rum==0:
                                    true=True
                                    break
                        time+=1    
                        for j in range(rum):
                            start=[start[0]+d[0][0],start[1]+d[0][1]]
                            sp[start[0]][start[1]]='   '+str(num)
                            num+=1
                    if true :break
        
                for i2 in range(s):
                    print(*sp[i2])
            print()
    except:break
                




