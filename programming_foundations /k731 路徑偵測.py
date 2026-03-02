n=int(input())
d=[1,0,0,0];now=[0,0];l=r=t=0#東南西北
for i in range(n):
    x,y=map(int,input().split())
    if x-now[0]>0:#
        if d[0]==1:
            pass
        elif d[1]==1:
            d=[1,0,0,0]
            l+=1
        elif d[2]==1:
            d=[1,0,0,0]
            t+=1
        elif d[3]==1:
            d=[1,0,0,0]
            r+=1
    elif y-now[1]<0:#對的
        if d[0]==1:
            d=[0,1,0,0]
            r+=1
        elif d[1]==1:
            pass
        elif d[2]==1:
            d=[0,1,0,0]
            l+=1
        elif d[3]==1:
            d=[0,1,0,0]
            t+=1
    elif y-now[1]>0:#
        if d[0]==1:
            d=[0,0,0,1]
            l+=1
        elif d[1]==1:
            d=[0,0,0,1]
            t+=1
        elif d[2]==1:
            d=[0,0,0,1]
            r+=1
        elif d[3]==1:
            pass
    
    elif x-now[0]<0:#
        if d[0]==1:
            d=[0,0,1,0]
            t+=1
        elif d[1]==1:
            d=[0,0,1,0]
            r+=1
        elif d[2]==1:
            pass
        elif d[3]==1:
            d=[0,0,1,0]
            l+=1
    now=[x,y]


print(l,r,t)
