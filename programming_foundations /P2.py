a=int(input())
m=[]
for i in range(a):
    m.append(list(input()))
sl=int(input())
s=[int(x) for x in input()]
ans=""
now=[[0,a-1],[0,a-1]]
for i in range(len(s)):
    if(s[i]==0):
        for i in range(a):
            if(now[0][0]+i>=0 and now[0][0]+i<a and now[0][1]+i>=0 and now[0][1]+i<a):
                ans+=m[now[0][0]+i][now[0][1]+i]
            else :break;
    else:
        for i in range(a):
            if(now[1][0]-i>=0 and now[1][0]-i<a and now[1][1]-i>=0 and now[1][1]-i<a):
                ans+=m[now[1][0]-i][now[1][1]-i]
            else :break;      
            
    if now[0][1]-1<0:
        now[0][0]+=1
    else: now[0][1]-=1

    if now[1][0]+1>=a:
        now[1][1]-=1
    else: now[1][0]+=1

print(ans)
