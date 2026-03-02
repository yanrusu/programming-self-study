#include <iostream>
#include <queue>
#include <algorithm>
using namespace std;

int main(){
    int n; cin>>n;
    int r,s,ans=0;
    queue <int> p;
    cin>>r>>s;  p.push(r+s);
    for(int i=1;i<n;i++){
        cin>>r>>s;
        while(!p.empty()&&p.front()<=r){p.pop();}
        if(p.empty()) p.push(r+s);
        else p.push(p.back()+s);
        ans = max(ans,(int)p.size()-1);        
    }
    cout<<ans<<'\n';
    
}