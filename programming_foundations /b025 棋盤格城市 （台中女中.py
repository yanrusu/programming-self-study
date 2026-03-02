cr=[[0]*32 for i in range(32)]

for i in range(1):
    for j in range(32):
        cr[i][j]=1
        cr[j][i]=1
      
for i in range(1,32):
    for j in range(1,32):
        cr[i][j]=cr[i-1][j]+cr[i][j-1]
        
