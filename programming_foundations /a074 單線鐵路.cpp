#include <bits/stdc++.h>
using namespace std;

int main(){
    ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);
    int N;
    while(cin>>N&&N!=0){
        int a[N];
        while(cin>>a[0]&&a[0]!=0){
            bool isOK=true;
            stack<int>stk; int p=1;
            for(int i=1;i<N;i++){
                cin>>a[i];
                }
            for(int i=0;i<N&&isOK;i++){
                if(a[i]>=p){
                    for(int j=p;j<a[i];j++) stk.push(j);
                    p=a[i]+1;
                }
            
                else if(a[i]==stk.top()){
                    stk.pop();
                }
                else isOK=0;
            }
            if(isOK) cout<<"Yes";
            else cout<<"No";
            cout<<'\n';
        }
        cout<<'\n';
    }

    return 0;
}