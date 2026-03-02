#include <bits/stdc++.h>
using namespace std;
long long p[50010];
long long cnt(int left,int right){
    if(right-left<=1) return 0;
    long long k=(p[left]+p[right])/2, len=p[right]-p[left];
    long long m=lower_bound(p+left,p+right,k)-p;
    if(p[right]-p[m]<=p[m-1]-p[left]) m--;
    
    return len+cnt(left,m)+cnt(m,right);
    
}
int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);cout.tie(0);
    int N,L;
    cin>>N>>L;
    p[0]=0;p[N+1]=L;
    for(int i=0;i<N;i++){
        cin>>p[i+1];
    }
    cout<<cnt(0,N+1);
    
}