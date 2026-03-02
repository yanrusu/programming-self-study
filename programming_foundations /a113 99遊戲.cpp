#include <bits/stdc++.h>
using namespace std;
map<int,queue<string>> mp;
int main(){
    for(int i=0;i<4;i++){
        char x;cin>>x;
        for(int j=0;j<13;j++){
            string s; cin>>s;
            mp[x-'A'].push(s);
        }
    }
    int sum=0,id=0,d=1;
    
    while(sum<=99){
        string card=mp[id].front();
        mp[id].pop();
        if(card=="A") sum=0;
        else if(card=="4") d*=-1;
        else if(card=="5");
        else if(card=="10"){
            sum+=10;
            if(sum>99) sum-=20;
        }
        else if(card=="J");
        else if(card=="Q"){
            sum+=20;
            if(sum>99) sum-=40;
        }
        else if(card=="K") sum=99;
        else{
            sum+=stoi(card);
            if(sum>99){
                cout<<char(id+'A')<<'\n'<<mp[id].size()<<'\n';
                break;
            }
            if(mp[id].empty()){
                cout<<char(id+'A')<<'\n'<<sum<<'\n';
                break;
            }
        }
        id=(id+d+4)%4;
        
    }
    
   
}