#include <iostream>
using namespace std;
int main(){
    ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);
    int a,ans=0; cin>>a;
    int p[a],vis[a]={0};
    for(int i=0;i<a;i++){
        cin>>p[i];
    }
    for(int i=0;i<a;i++){
        if(vis[i]) continue;
        int x=p[i];ans+=1;
        while(!vis[x]){
            vis[x]=1;
            x=p[x];
        }
    }
    
    cout<<ans<<'\n';

    return 0;
}