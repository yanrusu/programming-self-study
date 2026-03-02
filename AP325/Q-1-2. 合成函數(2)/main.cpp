#include <bits/stdc++.h>
using namespace std;
int expr(){
    char c[2];
    int x,y,z;
    scanf("%s",c);
    if (c[0]=='f'){
        // cout<<c<<endl;
        x=expr();
        return 2*x-3; 
    }
    else if(c[0]=='g'){
        // cout<<c<<endl;
        x=expr();
        y=expr();
        return 2*x+y-7;
    }
    else if(c[0]=='h'){
        // cout<<c<<endl;
        x=expr();
        y=expr();
        z=expr();
        return  3*x-2*y+z;
    }
    else{
        return atoi(c);
    }
}
int main(){
    cout<<expr();
}