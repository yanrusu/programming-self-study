#include <bits/stdc++.h>
using namespace std;

int s(int from[],int to[],int n){
    vector<int> v(from,from+n);
    sort(v.begin(),v.end());
    to[0]=v[0];
    int j=1;
    for(int i=1;i<n;i++) if(v[i]!=v[i-1]) to[j++]=v[i];
    return j;
}

int main(){
    ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);
    int n,a[100005],b[100005];
    cin>>n;
    for(int i=0;i<n;i++) cin>>a[i];
    int x=s(a,b,n);
    for(int i=0;i<n;i++) cout<<lower_bound(b,b+x,a[i])-b<<" ";
}
    