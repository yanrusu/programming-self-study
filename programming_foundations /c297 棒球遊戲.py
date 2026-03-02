re=[];sum_=0;counter=0;max_=0;base=[0,0,0];score=0;out=0;bk=False
for _ in range(9):
    a=input()
    a=a.split()
    sum_+=int(a[0]);
    if int(a[0])>max_:
        max_=int(a[0])
    re.append(a[1:])

outc=int(input())


for i in range(max_):
    if bk:break
    for j in range(9):
        counter+=1
        if counter>sum_:
            bk=True
            break

        if re[j][i]=='1B':
            if sum(base)==3:
                score+=1
            elif sum(base)==2:
                if base[0] and base[1]:
                    base=[1]*3
                elif base[1] and base[2]:
                    score+=1
                    base=[1,0,1]
                elif base[0] and base[2]:
                    score+=1
                    base=[1,1,0]
            elif sum(base)==1:
                if base[0]:
                    base[1]=1
                elif base[1]:
                    base=[1,0,1]
                elif base[2]:
                    base=[1,0,0]
                    score+=1
                    
            else: base[0]=1
        elif re[j][i]=='2B':
            if sum(base)==3:
                score+=2
                base=[0,1,1]
            elif sum(base)==2:
                if base[0] and base[1]:
                    score+=1
                    base=[0,1,1]
                elif base[1] and base[2]:
                    score+=2
                    base=[0,1,0]
                elif base[0] and base[2]:
                    score+=1
                    base=[0,1,1]
            elif sum(base)==1:
                if base[0]:
                    base=[0,1,1]
                elif base[1]:
                    score+=1
                    base=[0,1,0]
                elif base[2]:
                    score+=1
                    base=[0,1,0]
            else: base[1]=1
            

        elif re[j][i]=='3B':
            score+=sum(base)
            base=[0,0,1]

        elif re[j][i]=='HR':
            score+=sum(base)
            score+=1
            base=[0,0,0]

        else:
            out+=1
            if out%3==0:
                base=[0,0,0]
            if out==outc:
                bk=True
                break
        
print(score)
