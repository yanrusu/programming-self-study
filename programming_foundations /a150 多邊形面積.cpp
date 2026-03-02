#include <bits/stdc++.h>
using namespace std;

struct P{
    double x,y;  
};

int main()
{
    int n;cin>>n;
    double ans=0;
    P a[n];
    for(int i=0;i<n;i++){
        cin>>a[i].x>>a[i].y;
    }
    for(int i=0;i<n;i++){
        ans+=a[i].x*a[(i+1)%n].y-a[i].y*a[(i+1)%n].x;
    }

    cout<<setprecision(2)<<fixed<<abs(0.5*ans)<<'\n';
}