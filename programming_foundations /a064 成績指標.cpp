#include <bits/stdc++.h>
using namespace std;
int best=0,worst=100;

int main(){
    vector <int> b;
    int a; cin>>a;
    for(int i = 0 ; i<a;i++){
        int x; cin>>x;
        b.push_back(x);
        if(x>=60) worst=min(x,worst);
        else best=max(x,best);
    }
    sort(b.begin(),b.end());
    for(auto i:b){
        cout<<i<<' ';
    }
    cout<<'\n';
    if(!best) cout<<"best case"<<'\n';
    else cout<<best<<'\n';
    if(worst==100) cout<<"worst case"<<'\n';
    else cout<<worst<<'\n';
}