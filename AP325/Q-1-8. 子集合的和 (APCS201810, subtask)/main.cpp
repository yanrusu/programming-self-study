/*遞迴解
#include<bits/stdc++.h>
using namespace std;

int a[27],P,n,ans=0;

void sum(int idx,int s){
    if(idx>=n){
        if(s<P&&((P-s)<(P-ans))){
            ans=s;
        }
        return;    
    }
    int id=idx+1;
    
    
    
    sum(id,s+a[id]);
    sum(id,s);
}

int main(){
    ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);
    cin>>n>>P;
    for(int i=0;i<n;i++){
        cin>>a[i];
    }
    sum(-1,0);
    
    cout<<ans;
    
    
}*/

#include<bits/stdc++.h>
using namespace std;
int a[27],P,n,ans=0;
int main(){
    ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);
    cin>>n>>P;
    for(int i=0;i<n;i++){
        cin>>a[i];
    }
    for(int i=0;i<(1<<n);i++){ // i=0 == i=1
        int sum=0;
        for(int j=0;j<n;j++){
            if(i&(1<<j)){
                sum+=a[j];
            }
        }
        if((sum<P)&&(P-ans>P-sum)){
            ans=sum;
        }
    }
    
    
    cout<<ans;
    
    
}


