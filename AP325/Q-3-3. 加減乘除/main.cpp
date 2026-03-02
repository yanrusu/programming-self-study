#include <iostream>
#include <stack>
using namespace std;

int main(){
    stack<int> sta;
    int a; cin>>a;
    sta.push(a);
    char s;
    while(cin>>s>>a){
        if(s=='+'){
            sta.push(a);
        }
        else if(s=='-'){
            sta.push(-a);
        }
        else if(s=='*'){
            int t=sta.top();
            sta.pop();
            sta.push(t*a);
        }
        else{
            int t=sta.top();
            sta.pop();
            sta.push(t/a);
        }
    }
    long long result = 0;
    while(!sta.empty()){
        result += sta.top();
        sta.pop();
    }
    cout<<result;
}