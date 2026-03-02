#include <iostream>
#include <algorithm>
using namespace std;

int main()
{
    int n;cin>>n;
    int A[n];
    for(int i=0;i<n;i++) cin>>A[i];
    sort(A,A+n);
    cout<<A[0]<<" "<<A[n-1]<<" ";
    cout<<(A[n-1]-A[0]==n-1?"yes":"no");
}