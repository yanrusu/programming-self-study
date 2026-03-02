#include <bits/stdc++.h>
using namespace std;

int main(){
    int n,m,k,a[100005],b[100005],ans=0;
    cin>>n>>m>>k;
    for(int i=0;i<n;i++) cin>>a[i];
    for(int i=0;i<m;i++) cin>>b[i];
    sort(a,a+n);
    sort(b,b+m);
    int j=m-1;
    for(int i=0;i<n;i++){
        while((k-a[i]<=b[j])&&j>0){
            j--;
        }
        if(a[i]+b[j+1]==k) ans++;
    }
    cout<<ans<<'\n';
}