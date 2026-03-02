#include <bits/stdc++.h>
using namespace std;

int arr[502][502]={};

int main(){
    ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);
    int n,m,t;
    cin>>n>>m;
    cin>>t;
    for (int i=0;i<t;i++){
        int x1,x2,y1,y2,dx,dy;
        cin>>x1>>y1>>x2>>y2;
        dx=(x1==x2)?0:(x2-x1)/abs(x2-x1);
        dy=(y1==y2)?0:(y2-y1)/abs(y2-y1);
        for(int i=y1,j=x1;!(i==y2&&j==x2);i+=dy,j+=dx){
            arr[i][j]=1;
        }
        arr[y2][x2]=1;
    }
    int sum=0;
    for(int i=1;i<=m;i++){
        for (int j=1;j<=n;j++){
            sum+=arr[i][j];
        }
    }
    cout<<sum<<'\n';
}
