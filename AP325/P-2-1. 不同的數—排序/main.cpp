#include <bits/stdc++.h>
using namespace std;

int s(int from[],int to[],int n){
    sort(from,from+n);
    to[0]=from[0];
    int j=1;
    for(int i=1;i<n;i++){
        if(from[i]!=from[i-1]){
            to[j++]=from[i];
        }
    }
    return j;
    
}
int main(){
    ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);
    int n,a[100005],b[100005];
    cin>>n;
    for(int i=0;i<n;i++) cin>>a[i];
    int x=s(a,b,n);
    cout<<x<<'\n';
    for(int i=0;i<x;i++){
        cout<<b[i]<<" ";
    }
    
}