s=input()
a=int(input())
for i in range(len(s)):
    if a==1:
        if s[i].islower():
            print(s[i],end="")
    elif a==2:
        if s[i].isupper():
            print(s[i],end="")
    elif a==3:
        if s[i].isdigit():
            print(s[i],end="")
    
