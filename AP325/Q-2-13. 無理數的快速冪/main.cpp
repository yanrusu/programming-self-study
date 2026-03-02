#include <bits/stdc++.h>
using namespace std;
typedef long long LL;
#define P 1000000009

void ex(LL x,LL y,LL n){
    LL s=1,t=0,xi=x,yi=y,ti,ty,ts,tt;
    while(n>0){
        if(n&1){
            ts=s;tt=t;
            s=((ts*xi)%P+(2*tt*yi)%P)%P;
            t=((ts*yi)%P+(tt*xi)%P)%P;
        }
        ti=xi;ty=yi;
        xi=((ti*ti)%P+(2*ty*ty)%P)%P;
        yi=(2*ti*ty)%P;
        n>>=1;
    }
    cout<<s<<" "<<t<<'\n';
    return;
}


int main(){
    ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);
    LL x,y,n;
    cin>>x>>y>>n;
    ex(x,y,n);
}