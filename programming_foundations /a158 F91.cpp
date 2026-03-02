#include <iostream>
using namespace std;

int f(int a){
    if (a < 101) return f(f(a+11));
    else return a-10;
}

int main()
{
    int n;
    while (cin>>n){
        if (!n) break;
        cout<<"f91("<<n<<") = "<<f(n)<<'\n';
    }
}