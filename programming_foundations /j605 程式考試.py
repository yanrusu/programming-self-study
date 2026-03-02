n=int(input())
maxs=-1
maxst=0
error=0
for i in range(n):
    t,s=map(int,input().split())
    if s>maxs: maxst,maxs=t,s
    if s<0 : error+=1

if maxs-n-error*2>0: fs=maxs-n-error*2
else : fs=0
if maxs<0: maxs=0
print(fs,maxst)
