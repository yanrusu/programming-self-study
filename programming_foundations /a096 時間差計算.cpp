#include <bits/stdc++.h>
using namespace std;

int main()
{
    int a,b,c,a1,b1,c1;
    char r;
    cin>>a>>r>>b>>r>>c;
    cin>>a1>>r>>b1>>r>>c1;
    
    c = c1 - c;
    if(c<0){
        c+=60;
        b1-=1;
    }
    
    
    b = b1 - b;
    if(b<0){
        b+=60;
        a1-=1;
    }

    
    a = a1 - a;
    if(a<0){
        a+=24;
    }
    
    if(a<10) cout<<0<<a<<r;
    else cout<<a<<r;
    if(b<10) cout<<0<<b<<r;
    else cout<<b<<r;
    if(c<10) cout<<0<<c;
    else cout<<c<<'\n';
}
