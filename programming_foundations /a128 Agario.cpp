#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main(){
    ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);
    int n,m,maxi=0;cin>>n>>m;
    vector<int>v[n+1];
    for(int i=1;i<=n;i++) v[i].push_back(i);
    while(m--){
        int a,b; cin>>a>>b;
        if(v[a].size()>=v[b].size()){
            v[a].insert(v[a].end(),v[b].begin(),v[b].end());
            if(v[a].size()>v[maxi].size()) maxi=a;
        }
        else{
            for(auto i:v[a]) v[b].push_back(i);
            if(v[b].size()>v[maxi].size()) maxi=b;
        }
        
    }
    sort(v[maxi].begin(),v[maxi].end());
        cout<<maxi<<'\n';
        for(int i:v[maxi]) cout<<i<<" ";
}