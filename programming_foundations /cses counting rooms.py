n,m=map(int,input().split())
room=[]
for i in range(n):
    room.append(list(input()))
fc=0
for i in range(0,n):
    for j in range(0,m):
        if room[i][j]==".":
            fc+=1
            room[i][j]="#"
            q1=[];q2=[[i,j]]
            while q2:
                q1,q2=q2,q1
                while q1:
                    r,c=q1[0][0],q1[0][1]
                    if (r+1<n) and room[r+1][c]==".":
                            q2.append([r+1,c])
                            room[r+1][c]="#"
                    if  (r-1>=0)  and  room[r-1][c]==".":
                            q2.append([r-1,c])
                            room[r-1][c]="#"
                    if  (c+1<m) and room[r][c+1]==".":
                            q2.append([r,c+1])
                            room[r][c+1]="#"
                    if  (c-1>=0) and room[r][c-1]==".":

                            q2.append([r,c-1])
                            room[r][c-1]="#"

                    del q1[0]
print(fc)

                    

    
