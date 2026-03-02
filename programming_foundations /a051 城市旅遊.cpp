#include <iostream>
#include <vector>
using namespace std;

vector<int> C[801];
int vis[801];
bool dfs(int from, int to){
    vis[from]=1;
    for(int i=0;i<C[from].size();i++){
        if(vis[C[from][i]]) continue;
        if(C[from][i]==to){
            return true;}
        if(dfs(C[from][i],to)){return true;break;};
    }
    return false;
}

int main(){
    ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);
    int A,B,x,y;
    while(cin>>A>>B){
        for(int i=1;i<=A;i++){
            C[i].clear();
            vis[i]=0;
        }
        for(int i=0;i<B;i++){
            cin>>x>>y;
            C[x].push_back(y);
        }
        cin>>x>>y;
        if(dfs(x,y)) cout<<"Yes"<<'\n';
        else cout<<"No"<<'\n';
    }
}
