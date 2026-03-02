def check1():
    global a,cc
    for i1 in range(4):
        if a[i1]==1:
            cc0=i1+1
            break
def check3():
    global a,cc
    for i1 in range(4):
        if a[i1]==0:
            cc=i1+1




while True:
    r=int(input())
    if r==0:break
    m=[];yns=0;cr=cc=0;no=False;cc1=0

    for i in range(4):
        a=[int(x) for x in input().split()]
        m.append(a)
        if sum(a)%2!=0:
            if yns:
                no=True
                break
            yns+=1
            cr=i+1
            if sum(a)==1:
                check1()     
            else:
                check3()

    no1=False
    for i in range(4):
        csum=0
        if no1: break
        for j in range(4):
            csum+=m[j][i]
            if j==3:
                if csum!=2:
                    if i!=cr:
                        no1=True
                        break
                        
            
            


                   
    if no or no1:print("Corrupt")
    elif yns==1 :print(f"Change bit ({cr},{cc})")
    else:print("OK")
