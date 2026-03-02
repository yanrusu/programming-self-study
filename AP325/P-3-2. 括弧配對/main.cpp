#include <bits/stdc++.h>
using namespace std;

int main(){
    string s;
    while(getline(cin, s)){
        bool isOk=true;
        stack<char> sta;
        for(int i=0;i<s.size();i++){
            if(s[i]=='('||s[i]=='{'||s[i]=='['){
                sta.push(s[i]);
            }
            else{
                if(sta.empty()){
                    isOk=false;
                    break;
                }
                else{
                    char ts = sta.top(); sta.pop();
                    if(s[i]==')'&&ts=='('){
                        
                    }
                    else if(s[i]==']'&&ts=='['){
                        
                    }
                    else if(s[i]=='}'&&ts=='{'){
                        
                    }
                    else{
                        isOk=false;
                    }
                }
            }
        }
        if(!sta.empty()) isOk=false;
        if(isOk) cout<<"yes\n";
        else cout<<"no\n";
    }
}