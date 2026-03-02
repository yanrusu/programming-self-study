a=int(input())
s=input()
coub=0
cous=0
len_=[]
for i in range(len(s)):
    if 'A'<=s[i]<='Z':
        if cous!=0:
            len_.append(cous)
            cous=0
        coub+=1
        if i==len(s)-1:
            len_.append(coub)
        
    else:
        if coub!=0:
            len_.append(coub)
            coub=0
        cous+=1
                
        if i==len(s)-1:
            len_.append(cous)
oa=[]
co=0
len_len=len(len_)
for i in range(len_len):
    if len_[i]!=a:
        if len_[i]>a:
            len_[i]=-1
        
        else: len_[i]=0
for i in range(len_len):
    try :
        if len_[i]==-1 and len_[i+1]==-1:
            len_.pop(i+1)
            co+=1
    except:pass
   

t=0
for i in range(len_len-co):
    if len_[i]== 0 or len_[i]==  -1:
        oa.append(len_[t:i+1])
        t=i
try:        
    x=max(oa,key=len)
    for i in range(x.count(0)):
        x.remove(0)
    print(len(x)*a)
except: print(a)

   


