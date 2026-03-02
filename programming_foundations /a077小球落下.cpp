#include <iostream>
using namespace std;

int main(){
    ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);
    int n;cin>>n;
    while(n--){
        int x,t,idx;cin>>x>>t;
        int bt[2048]={0};
        for(int i=0;i<t;i++){
            idx=1;
            for(int j=1;j<x;j++){
                int nxt=idx*2+bt[idx];
                bt[idx]=!bt[idx];
                idx=nxt;
            }
        }
        cout<<idx<<'\n';
    }

    return 0;
}