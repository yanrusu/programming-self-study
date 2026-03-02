#include <bits/stdc++.h>
using namespace std;

int main(){
    ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);
    int n,ans=0;
    long long a[26];
    cin>>n;
    for(int i=0; i<n; i++) cin>>a[i];
    for(int i=1;i<(1<<n);i++){
        long long p=1;
        for(int j=0;j<n;j++){
            if(i&(1<<j)){
                p=p*a[j]%10009;
            }
        }
        if(p==1) ans++;
    }
    
    cout<<ans<<'\n';
}