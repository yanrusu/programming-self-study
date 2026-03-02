#include <iostream>
using namespace std;

int main(){
    ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);
    int n;cin>>n;
    int a[n];
    for(int i=0;i<n;i++){
        cin>>a[i];
    }
    int key;cin>>key;
    int L=0,R=n-1,M,tm=0;
    bool check=0;
    while(L<=R){
        tm++;
        M=(L+R)/2;
        if(a[M]>key){R=M-1;}
        else if(a[M]<key){L=M+1;}
        else if(a[M]==key){
            check=1;
            break;
        }
        }
    if(check) cout<<M<<" "<<tm<<'\n';
    else cout<<"not found "<<tm<<'\n';
}