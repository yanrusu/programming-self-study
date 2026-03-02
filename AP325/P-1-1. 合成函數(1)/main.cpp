#include <bits/stdc++.h>
using namespace std;
int expr(){
    int x,y;
    char str[1];
    scanf("%s",str);
    if(str[0]=='f'){
        x=expr();
        return x*2-1;
    }
    else if(str[0]=='g'){
        x=expr();
        y=expr();
        return x+2*y-3;
    }
    else{
        return atoi(str);
    }
}
int main(){
    cout<<expr();
}