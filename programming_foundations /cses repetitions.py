n=input()
now=1;ans=[]
for i in range(len(n)-1):
    if n[i]==n[i+1]:
        now+=1
    else :
        ans.append(now)
        now=1
ans.append(now)
print(max(ans))
