#include <bits/stdc++.h>
using namespace std;
int p[50010],k=0,K;
long long cut(int left,int right,int a){
    if (a>=K || right-left<=2){
        // cout<<right<<" "<<left<<'\n';
        return 0;
    } 
    vector<long long>s;
    for(int i=left+1;i<right;i++){
        long long lsum=0,rsum=0;
        for(int y=left;y<i;y++){
            lsum+=p[y]*(y-i);
            // cout<<p[y]*(y-i)<<" ";
        }
        for(int z=i+1;z<=right;z++){
            rsum+=p[z]*(z-i);
        }
        // cout<<'\n';
        s.push_back(abs(abs(lsum)-rsum));
        // cout<<abs(abs(lsum)-rsum)<<" "<<'\n';
    }
    int minidx = min_element(s.begin(),s.end())-s.begin();
    // cout<<"minidx"<<minidx<<'\n';
    int val=p[left+1+minidx];
    // cout<<"val"<<val<<'\n';
    k++;
    // cout<<"k"<<k<<'\n';
    // cout<<"nleft"<<left+minidx<<'\n'<<"nright"<<left+2+minidx<<'\n';
    return val+cut(left,left+minidx,k)+cut(left+2+minidx,right,k);
    
    
}


int main(){
    ios::sync_with_stdio(0);cin.tie(0);cout.tie(0);
    int N;
    cin>>N>>K;
    for(int i=0;i<N;i++){
        cin>>p[i];
    }
    cout<<cut(0,N-1,k);
    return 0;
}