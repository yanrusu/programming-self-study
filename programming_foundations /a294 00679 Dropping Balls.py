def runtree(n):
    global depth,treebool,targetball

    if 2**(depth-1)<=n<2**depth:
        if targetball:
            print(n)
            return 
            
        return 
    if treebool[n-1]:
        treebool[n-1]=False
        runtree(2*n+1)
        
    else:
        treebool[n-1]=True
        runtree(2*n)

while True:
    try:
        for i in range(int(input())):
            depth,tor=map(int,input().split())
            treebool=[False]*(2**depth-1)
            targetball=False
            for i in range(tor):
                if i==tor-1:
                    targetball=True
                
                    
                runtree(1)
    except:break
