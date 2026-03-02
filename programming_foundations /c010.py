import bisect
def oe():
    global ll
    if len(ll)%2!=0:
        print(ll[len(ll)//2])
    else: print((ll[len(ll)//2]+ll[(len(ll)//2)-1])//2)
ll=[]
while True:
    try:
        n=int(input())
        if len(ll)<=1:
            ll.append(n)
        elif ll[0]>n:
            ll.insert(0,n)
        elif ll[-1]<n:
            ll.append(n)
        else:
            '''for i in range(len(ll)-1):
                if ll[i]<n and ll[i+1]>n:
                    ll.insert(i+1,n)'''
            bisect.insort(ll,n)
        oe()
    except:break
