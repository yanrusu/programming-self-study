#include <bits/stdc++.h>
using namespace std;

long long ex(int x,int y,int p){
    long long xi=x, t=1;
    while(y>0){
        if(y&1) t=(t*xi)%p;
        xi=(xi*xi)%p;
        y>>=1;
    }
    return t;
    
    
}


int main(){
    ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);
    int n,p;
    cin>>n>>p;
    for(int i=0;i<n;i++){
        int x; cin>>x;
        cout<<ex(x,p-2,p)<<" ";
    }
    // int x; cin>>x;
    // cout<<ex(x,p-2,p)<<'\n';
}