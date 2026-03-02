m,n=map(int,input().split())
a=[[0]*n for i in range(m)]
s=''
for i in range(m):
    x=input()
    x=x[::-1]
    for j in range(n):
        a[i][j]=x[j]
t=input()
a=a[::-1]
for i in range(m):
    coun=0
    s=''
    t=t[::-1]
    for j in range(n):
        if a[i][j]=='0':
            s=t[j]+s
        else :
            s=s+t[j]
            coun+=1
    if coun%2!=0:
        if len(t)%2==0:
            s=s[len(t)//2:]+s[0:len(t)//2]
        else:s=s[len(t)//2+1:]+s[len(t)//2:len(t)//2+1]+s[0:len(t)//2]
        

    t=s
print(t)







'''

slice

思考
        
'''

    
