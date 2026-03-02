R,C,M = map(int,input().split())
C1=C+1;R1=R+1
a=[[0]*C1 for i in range(R1)]
aturn=[[0]*R1 for i in range(C1)]
for i in range(R):
    t=[int(x) for x in input().split()]
    for j in range(C):
        a[i][j]=t[j]
con=[int(x) for x in input().split()]
con=con[::-1]
for i in range(M):
    if con[i]==0:
        for i in range(R):
            for j in range(C):
                aturn[i][j]=a[j][C-1-j]
               

'''
                1(11)(13) 5(12)
                3(21)(12) 1(22)
                4(31)(11) 2(32)[][c]    3-1-2=0
                
                4(10) 3(11) 1(12)
                2(21) 1(22) 5(23)1
                [c][]  3(12) 3-1-1  3-2-1=0
               
        else :
            for i in range(R):
                for j in range(C):
                '''
               
    
'''
1(1,1)2
3(2,1) 4
5(3,1) 6
7(4,1) 8

7(1,1) 5(1,2) 3(1,3) 1(1,4)
8 6 4 2
'''

        
