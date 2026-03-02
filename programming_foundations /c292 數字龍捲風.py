'''以官方題目提示:本題有多種處理方式,其中之一是觀察每次轉向與走的步數。例如,起始方向是向
左時,前幾步的走法是:左 1、上 1、右 2、下 2、左 3、上 3、......一直到出界為止。'''

def run_():
    global i,t,a,map_,nowr,nowc
    while True:
        i+=1
        if i%2==0: t=t+1#如果跑兩次了，增加同一方向次數
        for _ in range(t):
            if not ((nowr+a[0][0]>n-1) or (nowr+a[0][0]<0) or (nowc+a[0][1]>n-1) or (nowc+a[0][1]<0)):#判斷出界
                nowr,nowc=nowr+a[0][0],nowc+a[0][1]#移動當前位置
                print(map_[nowr][nowc],end='')
                if _==t-1:
                    tem=a[0]
                    a=a[1:]+[tem]#如果當前的方向跑完，移動方向依上、右、下、左循環
        if i==n*n-2: break #當次數等於數字次數結束，因為剛開始令-1所以要減2



n=int(input())
d=int(input())
map_=[]
nowr=nowc=n//2
for i in range(n):
    map_.append([int(x) for x in input().split()])
print(map_[nowr][nowc],end='')
f=False
if d==0:
    i=-1#紀錄次數
    t=0#控制同一方向移動次數
    a=[[0,-1],[-1,0],[0,1],[1,0]]#移動方向順序
    run_()
elif d==1:
    i=-1
    t=0
    a=[[-1,0],[0,1],[1,0],[0,-1]]
    run_()
elif d==2:
    i=-1
    t=0
    a=[[0,1],[1,0],[0,-1],[-1,0]]
    run_()

elif d==3:
    i=-1
    t=0
    a=[[1,0],[0,-1],[-1,0],[0,1]]
    run_()

            
        
        
        
        

    
