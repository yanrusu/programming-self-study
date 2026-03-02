n,m=map(int,input().split())
s=[int(x) for x in input().split()]
t=[int(x) for x in input().split()]
r=[int(x) for x in input().split()]
wl=[0]*n
while len(r)!=1:
    w=[];l=[]
    
    if len(r)%2 != 0:
        l.append(r[-1])
        r.pop()
    for i in range(0,len(r),2):
        f=r[i]-1
        f1=r[i+1]-1
        a,b,c,d=s[f],t[f],s[f1],t[f1]
        if s[f]*t[f]>=s[f1]*t[f1]:
            s[f]=a + (c*d)//(2*b)
            t[f]=b + (c*d)//(2*a)
            s[f1]=c + (c//2)
            t[f1]=d + (d//2)
            wl[f1]+=1
            w.append(f+1)
            l.append(f1+1)
        
        else:
            s[f1]=c + (a*b)//(2*d)
            t[f1]=d + (a*b)//(2*c)
            s[f]=a + (a//2)
            t[f]=b + (b//2)
            wl[f]+=1 
            w.append(f1+1)
            l.append(f+1)
        
        if m in wl : 
            for i in range(wl.count(m)):
                a=wl.index(m)
                wl[a]=-1
                a+=1
                l.remove(a)
    
    
    r=w+l
print(*r)
        
    
        
