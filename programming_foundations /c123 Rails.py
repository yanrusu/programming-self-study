while True:
        t=int(input())
        if t==0:break
        a=[i+1 for i in range(t)]
        while True:
            f=[int(x) for x in input().split()]
            if f[0]==0:break
            yn=True
            stacka=a[::]
            sta=[]
            while True:
                if sta and f[0]==sta[-1]:
                    del f[0]
                    del sta[-1]
                elif stacka:
                    sta.append(stacka[0])
                    del stacka[0]
                elif sta and f and len(stacka)==0 and f[0]!=sta[-1]:
                    yn=False
                    break
                elif len(sta)==0 and len(f)==0 and len(stacka)==0:
                    break
            if yn:print("Yes")
            
            else :print("No")
            
                    
   
