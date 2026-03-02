t=int(input())
queue=[]
for _ in range(t):
    opea=[int(x) for x in input().split()]
    if opea[0]==1:
        queue.append(opea[1])
    elif opea[0]==2:
        if queue:
            print(queue[0])
        else: print(-1)

    else :
        if queue:
            queue.pop(0)
        
