#include <iostream>
using namespace std;
#define N 70

int main()
{
    ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);
    int n; cin>>n;
    int A[N]={0},E[N]={0},T[N]={0};
    A[0]=1;T[0]=1;E[0]=3;
    for(int i = 2 ; i<=n;i++){
        for(int j = 0;j<N;j++){
            T[j]+=E[j];
            E[j]*=4;
            A[j]+=T[j];
        }
        for(int j=0;j<N-1;j++){
            A[j+1]+=A[j]/10;A[j]=A[j]%10;
            T[j+1]+=T[j]/10;T[j]=T[j]%10;
            E[j+1]+=E[j]/10;E[j]=E[j]%10;
        }
    }
    
    int k = N-1;
    while(!A[k]) k--;
    for(;k>=0;k--) cout<<A[k];
    cout<<'\n';
}