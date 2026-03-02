def iw():
    global a
    for i in range(4):
        a[i]=int(a[i])
    


while True:
    r=int(input())
    if r==0:break
    m=[];rers=cers=cr=cc=0;no=False;problom=[]
    for i in range(4):
        a=list(input())
        iw()
        if sum(a)%2!=0:
            rers+=1
            problom.append(i)
            if rers>1:no=True
        m.append(a)
    if no :
        print("Corrupt")
        break
    for i in range(4):
        rsum=csum=0
        if no:break
        for j in range(4):
            rsum+=m[i][j]
            csum+=m[j][i]
            if j==3:
                if csum!=2:
                    if csum==4:
                        no=True
                        break
                    cers+=1
                    if cers>1:
                        no=True
                        break
                
                        
    if no :
        print("Corrupt")
        break
    
    if cers or rers :
        cr=problom[0]
        for j in range(4):
            if m[cr][j]==1 and m[j][cr]==1:
                cc=j+1 ;cr=cr+1
                break
                        
            

            
            


                   
    if no :print("Corrupt")
    elif cc and cr :print(f"Change bit ({cr},{cc})")
    else:print("OK")
