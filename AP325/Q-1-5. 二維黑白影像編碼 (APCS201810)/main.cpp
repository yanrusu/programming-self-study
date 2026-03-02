#include <bits/stdc++.h>
using namespace std;
string s;
int cnt=0,n,idx=-1;

void ex(int a){
    idx++;
    char ns=s[idx];
    if(ns=='2'){
        a=a/2;
        for(int i=0;i<4;i++){
            ex(a);    
        }
        return;
    }
    else if(ns=='1'){
        cnt+=a*a;
        return;
    }
    else{
        return;
    }
}

int main(){
    ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);
    getline(cin,s);
    cin>>n;
    ex(n);
    cout<<cnt<<'\n';
}