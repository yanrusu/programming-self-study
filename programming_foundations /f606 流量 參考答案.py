## Python language
 
n,m,k=map(int,input().split())
flow=[]
for i in range(n): flow.append([int(x) for x in input().split()])
ANS=[]
for i in range(k):
    router=[[] for _ in range(m)]
    plan=[int(x) for x in input().split()]
    for j in range(n): router[plan[j]].append(j)
    ans=0
    for From in range(m):
        for To in range(m):
            if From==To:
                sum_flow=0
                if router[From]==[]: continue
                sum_flow += sum([flow[i][To] for i in router[From]])
                ans+=sum_flow
            else:
                sum_flow=0
                if router[From]==[]: continue
                sum_flow += sum([flow[i][To] for i in router[From]])
                if sum_flow<=1000: ans+=sum_flow*3
                elif sum_flow>1000: ans+=3000+(sum_flow-1000)*2
    ANS.append(ans)
print(min(ANS))
