brotherf=[int(input())]
sister_n=int(input())
sisterf=list(int(x) for x in input().split())

#if brotherf == 2: brotherf=-brotherf
#for i in range (sister_n):
 #   if sisterf[i]==2: sisterf[i]==-2
brotherf.append(sisterf[0])
for i in range (1,sister_n):
    if sisterf[i]==sisterf[i-1]:
        if sisterf[i]==2:
            brotherf.append(0)
        elif sisterf[i]==0:
            brotherf.append(5)
        else:
            brotherf.append(2)
    else :
        brotherf.append(sisterf[i])
for i in range(sister_n):
    if sisterf[i]==0 and brotherf[i]==2:
        print(*brotherf[0:i+1],": Lost at round",i+1)
        break
    elif sisterf[i]==5 and brotherf[i]==0:
        print(*brotherf[0:i+1],": Lost at round",i+1)
        break
    elif sisterf[i]==2 and brotherf[i]==5:
        print(*brotherf[0:i+1],": Lost at round",i+1)
        break
    elif sisterf[i]==5 and brotherf[i]==2:
        print(*brotherf[0:i+1],": Won at round",i+1)
        break
    elif sisterf[i]==2 and brotherf[i]==0:
        print(*brotherf[0:i+1],": Won at round",i+1)
        break
    elif sisterf[i]==0 and brotherf[i]==5:
        print(*brotherf[0:i+1],": Won at round",i+1)
        break
    elif i+1==sister_n:
        print(*brotherf[0:i+1],": Drew at round",i+1)
        break

   









#for i in range(stsrer_n):
 #   if sisterf[i]>brotherf: print(brotherf,": Lost at round")
  #  elif sisterf[i]<brotherf: print(brotherf,": Won at round")
   # break

    #if sisterf[i]==sisterf[i-1]:
     #   brotherf.append(sisterf[i])
      #  brotherf.append(sisterf[i])
       # if sisterf[i]>brotherf[i]: print(*brotherf ": Lost at round ")
        




















   # if (sisterf[0]==0 and brotherf==2) or (sisterf[0]==5 and brotherf==0) or (sisterf[0]==2 and brotherf==5):
    #    print(brotherf,": Lost at round")
    #elif (sisterf[0]==2 and brotherf==0) or (sisterf[0]==0 and brotherf==5) or (sisterf[0]==5 and brotherf==2):
     #   print(brotherf,": Won at round")

