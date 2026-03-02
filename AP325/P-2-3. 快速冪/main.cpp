#include <bits/stdc++.h>
using namespace std;
int p;

long long ex(long long x,long long y){
    if(y<=0) return 1;
    if(y%2!=0) return (ex(x,y-1)*x)%p;
    long long t=ex(x,y/2);
    return (t*t)%p;
}


int main(){
    ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);
    long long x,y;
    cin>>x>>y>>p;
    cout<<ex(x,y)<<'\n';
    
}