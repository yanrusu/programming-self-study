K,Q,R=map(int,input().split())
a=list(input())
pa=""
for i in range(Q):
    a1=[int(x) for x in input().split()]
    for i in range(len(a)):
        if a1[i]==1 :
            na=a[i]
       
        elif a1[i]==2 :
            nb=a[i]

        elif a1[i]==3 :
            nc=a[i]
    
        elif a1[i]==4 :
            nd=a[i]
        elif a1[i]==5: ne=a[i]
        elif a1[i]==6: nf=a[i]
        elif a1[i]==7: ng=a[i]
        elif a1[i]==8: nh=a[i]
        elif a1[i]==9: nm=a[i]
        elif a1[i]==10: nn=a[i]
        elif a1[i]==11: nj=a[i]
        elif a1[i]==12: nk=a[i]
        elif a1[i]==13: nq=a[i]
        elif a1[i]==14: nr=a[i]
        elif a1[i]==15: ns=a[i]
        elif a1[i]==16: nt=a[i]
        elif a1[i]==17: nu=a[i]
        elif a1[i]==18: nv=a[i]
        elif a1[i]==19: nx=a[i]
        elif a1[i]==20: ny=a[i]
    if K==1: a=[na]
    if K==2: a=[na,nb]
    if K==3: a=[na,nb,nc]
    if K==4: a=[na,nb,nc,nd] 
    if K==5: a=[na,nb,nc,nd,ne] 
    if K==6: a=[na,nb,nc,nd,ne,nf]
    if K==7: a=[na,nb,nc,nd,ne,nf,ng]
    if K==8: a=[na,nb,nc,nd,ne,nf,ng,nh]
    if K==9: a=[na,nb,nc,nd,ne,nf,ng,nh,nm]
    if K==10: a=[na,nb,nc,nd,ne,nf,ng,nh,nm,nn] 
    if K==11: a=[na,nb,nc,nd,ne,nf,ng,nh,nm,nn,nj]
    if K==12: a=[na,nb,nc,nd,ne,nf,ng,nh,nm,nn,nj,nk]
    if K==13: a=[na,nb,nc,nd,ne,nf,ng,nh,nm,nn,nj,nk,nq]
    if K==14: a=[na,nb,nc,nd,ne,nf,ng,nh,nm,nn,nj,nk,nq,nr]
    if K==15: a=[na,nb,nc,nd,ne,nf,ng,nh,nm,nn,nj,nk,nq,nr,ns]
    if K==16: a=[na,nb,nc,nd,ne,nf,ng,nh,nm,nn,nj,nk,nq,nr,ns,nt]
    if K==17: a=[na,nb,nc,nd,ne,nf,ng,nh,nm,nn,nj,nk,nq,nr,ns,nt,nu]
    if K==18: a=[na,nb,nc,nd,ne,nf,ng,nh,nm,nn,nj,nk,nq,nr,ns,nt,nu,nv]
    if K==19: a=[na,nb,nc,nd,ne,nf,ng,nh,nm,nn,nj,nk,nq,nr,ns,nt,nu,nv,nx]
    if K==20: a=[na,nb,nc,nd,ne,nf,ng,nh,nm,nn,nj,nk,nq,nr,ns,nt,nu,nv,nx,ny]
    for i in range(R): pa+=a[i]
print(pa)
        
        
  #elif a1[i]==6: ne=a[i]
   #     elif a1[i]==7: ne=a[i]
    #    elif a1[i]==8: ne=a[i]
      #   elif a1[i]==9: ne=a[i]
  #       elif a1[i]==10: ne=a[i]
    #     elif a1[i]==11: ne=a[i]
      #   elif a1[i]==12: ne=a[i]
   #      # elif a1[i]==13: ne=a[i]
  #       elif a1[i]==14: ne=a[i]
   #    elif a1[i]==5: ne=a[i]
