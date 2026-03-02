#include <iostream>
using namespace std;

long long fun(string x){
    string s;
    long long ways=1,w=0;
    while(cin>>s){
        if(s==x) break;
        if(s=="IF"){
            w=fun("ELSE");
            w+=fun("END_IF");
            ways*=w;
        }
    }
    return ways;
    
}

int main()
{
    ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);
    int n;cin>>n;
    while(n--) cout<<fun("ENDPROGRAM")<<'\n';

}