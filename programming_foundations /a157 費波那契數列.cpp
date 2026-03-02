#include <iostream>
using namespace std;

unsigned long long f(int a){
    if(a==0)return 0;
    else if(a==1) return 1;
    else return f(a-1)+f(a-2);
}

int main(){
    ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);
    int n;
    while(cin>>n){
    cout<<f(n)<<'\n';
}
}