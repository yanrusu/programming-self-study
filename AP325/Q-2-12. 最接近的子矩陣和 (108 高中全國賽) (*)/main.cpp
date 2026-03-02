#include <bits/stdc++.h>
using namespace std;
typedef long long ll;


int main(){
    ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);
    int k,N,M;  cin>>k>>M>>N;
    ll ans=LLONG_MIN;
    vector<vector<int>> matrix(M,vector<int>(N));
    for(int i=0;i<M;i++){
        for(int j=0;j<N;j++){
            cin>>matrix[i][j];
        }
    }

    for(int i=0;i<M;i++){
        vector<ll> v(N,0);
        for(int j=i;j<M;j++){
            set<ll> ps({0}); ll psum=0;
            for(int z=0;z<N;z++){
                v[z]+=matrix[j][z];
                psum+=v[z];
                auto idx=ps.lower_bound(psum-k);
                if(idx!=ps.end()){
                    if(psum-*idx>ans) ans=psum-*idx;
                }
                ps.insert(psum);
           }
           if(ans==k) break;
        }

    }
    cout<<ans<<'\n';
}

#include <bits/stdc++.h>
using namespace std;


//best
/*int main(){
    ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);
    int k,N,M;  cin>>k>>M>>N;
    long long ans=LLONG_MIN;
    vector<vector<int>> matrix(M,vector<int>(N));
    for(int i=0;i<M;i++){
        for(int j=0;j<N;j++){
            cin>>matrix[i][j];
        }
    }

    for(int i=0;i<M;i++){
        vector<long long> v(N,0);
        for(int j=i;j<M;j++){
            set<long long> ps({0}); long long psum=0;
            for(int z=0;z<N;z++){
                v[z]+=matrix[j][z];
                psum+=v[z];
                auto idx=ps.lower_bound(psum-k);
                if(idx!=ps.end()){
                    if(psum-*idx>ans) ans=psum-*idx;
                }
                ps.insert(psum);
           }
          
        }
        if(ans==k) break;
    }
    cout<<ans<<'\n';
}*/