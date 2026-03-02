n=int(input())
a=[]
for i in range(n):
    s=list(input())
    a.append(s)
q1=[[1,1]]
q2=[]
f=1
n1=n-2
st=False
while True:
    if f%2==1:
        f+=1
        i=0
        while len(q1)!=0:
            r,c=q1[i][0],q1[i][1]
            a[r][c]=-1
            if a[r+1][c]=='.':
                q2.append([r+1,c])
                a[r+1][c]=-1
                if r+1 ==n1 and c == n1:
                    print(f)
                    st=True
                    break
            if a[r-1][c]=='.':
                q2.append([r-1,c])
                a[r-1][c]=-1
                if r-1==n1  and c == n1:
                    print(f)
                    st=True
                    break
            if a[r][c+1]=='.':
                q2.append([r,c+1])
                a[r][c+1]=-1
                if r ==n1 and c+1 == n1:
                    print(f)
                    st=True
                    break
            if a[r][c-1]=='.':
                q2.append([r,c-1])
                a[r][c-1]=-1
                if r ==n1 and c+1 == n1:
                    print(f)
                    st=True
                    break
            del q1[i]
    
            
    else:
        f+=1
        i=0
        while len(q2) !=0:
            r,c=q2[i][0],q2[i][1]
            a[r][c]=-1
            if a[r+1][c]=='.':
                q1.append([r+1,c])
                a[r+1][c]=-1
                if r+1==n1  and c == n1:
                    print(f)
                    st=True
                    break
            if a[r-1][c]=='.':
                q1.append([r-1,c])
                a[r-1][c]=-1
                if r-1==n1  and c == n1:
                    print(f)
                    st=True
                    break
            if a[r][c+1]=='.':
                q1.append([r,c+1])
                a[r][c+1]=-1
                if r==n1  and c+1 == n1:
                    print(f)
                    st=True
                    break
            if a[r][c-1]=='.':
                q1.append([r,c-1])
                a[r][c-1]=-1
                if r ==n1 and c+1 == n1:
                    print(f)
                    st=True
                    break
            del q2[i]
    if st :break
 
    if len(q1)==0 and len(q2)==0: break

if len(q1)==0 and len(q2)==0: print('No solution!')       
