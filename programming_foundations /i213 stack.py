t=int(input())
stack=[]
for _ in range(t):
    opea=[int(x) for x in input().split()]
    if opea[0]==1:
        stack.append(opea[1])
    elif opea[0]==2:
        if stack:
            print(stack[-1])
        else: print(-1)

    else :
        if stack:
            stack.pop()
        
