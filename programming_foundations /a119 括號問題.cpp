#include <bits/stdc++.h>
using namespace std;
int main(){
    stack <char> a;
    string x;
    int ans=0;
    cin>>x;
    for(int i=0;i<x.size();i++){
        if(x[i]=='('){
            a.push(x[i]);
        }
        else{
            if(a.empty()){
                ans=0;
                break;
            }
            else{
                a.pop();
                ans+=1;
            }
        }
    }
        
    if(!a.empty()) ans=0;
    cout<<ans<<'\n';
}
