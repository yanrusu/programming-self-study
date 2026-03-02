#include <bits/stdc++.h>
using namespace std;

int main(){
    ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);
    int n,K,a,psum=0;
    cin>>n>>K;
    int ans=0;
    set<int> S({0});
    for(int i=0;i<n;i++){
        cin>>a;
        psum+=a;
        auto idx=S.lower_bound(psum-K);
        if(idx!=S.end()){
            if(psum-*idx>ans) ans=psum-*idx;
        }
        S.insert(psum);
    }
    cout<<ans<<'\n';
}