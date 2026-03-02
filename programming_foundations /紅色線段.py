n,k=map(int,input().split())
a=[int(x) for x in input().split()]
alen=len(a)
maxl=0;minl=0
def long(a):
    global maxl
    global minl
    global b
    j=0
    for i in range(len(a)):
            j+=1
            red_l=0
            if va[i]==True: continue
            if a[i]==1:
                while a[i] != 0: #當j!=等於零 計算長度
                    va[i]=True
                    i+=1
                    red_l+=1
                    if i==len(a):break
                b.append(red_l)
            if j==alen:
                maxl+=max(b)
                minl+=min(b)
            
if k==0:
    b=[]
    va=[False]*alen
    long(a)
    '''
    for i in range(len(a)):
        red_l=0
        if va[i]==True: continue
        if a[i]==1:
            while a[i] != 0: #當j!=等於零 計算長度
                va[i]=True
                i+=1
                red_l+=1
                if i==len(a):break
            b.append(red_l)
            '''
    print(max(b))
    print(min(b))       

else:
    cha=[int(x) for x in input().split()]
    b=[]
    va=[False]*alen
    long(a)
    '''for i in range(len(a)):
        red_l=0
        j+=1
        print(j)
        if va[i]==True: continue
        if a[i]==1:
            while a[i] != 0: #當j!=等於零 計算長度
                va[i]=True
                i+=1
                red_l+=1
                if i==len(a):break
            b.append(red_l)
        if j==alen:
            maxl+=max(b)
            minl+=min(b)
            print(j)'''
    for i in range(k):
        chai=cha[i]-1
        a[chai]=1
        b=[]
        va=[False]*alen
        long(a)
        '''
        for i in range(len(a)):
            j+=1
            red_l=0
            if va[i]==True: continue
            if a[i]==1:
                while a[i] != 0: #當j!=等於零 計算長度
                    va[i]=True
                    i+=1
                    red_l+=1
                    if i==len(a):break
                b.append(red_l)
            if j==alen:
                maxl+=max(b)
                minl+=min(b)
                print(i)'''
    print(maxl)
    print(minl)
            
