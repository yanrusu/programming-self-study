#include <iostream>
#include <stack>
using namespace std;

int main(){
    int n; cin>>n;
    int h[200000],hp[200000];
    long long ans;
    for(int i=0;i<n;i++){
        cin>>h[i];
    }
    for(int i=0;i<n;i++){
        int t;cin>>t;
        hp[i]=t+h[i];
    }
    set<int> S={0}
    for(int i=1;i<n;i++){
        while(h[S.top()]<h[i])
            h.pop();
        
    }
}