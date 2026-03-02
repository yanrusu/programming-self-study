t=int(input())
for i in range(t):
    yn=False
    num=0
    stack=[]
    s=list(input())
    while s:
        if s[0]=="(":
            num+=1
            stack.append(s.pop(0))
        elif s[0]==")" :
            if not stack :
                yn=True
                break
            s.pop(0)
            stack.pop()
        else : #測資裡面有空白 XD
            if s[0]==" ": s.pop(0)
    if s or stack or yn:
        print(0)
    else:   print(num)
        
     
