#include <bits/stdc++.h>
using namespace std;

struct animal{
    string name;
    int sum;
};

struct location{
    string name;
    vector<animal>ani;
};

vector<location> l;
void insert(string a,int n,string p){
    for(int i=0;i<l.size();i++){
        if(l[i].name==p){
            for(int j=0;j<l[i].ani.size();j++){
                if(l[i].ani[j].name==a){
                    l[i].ani[j].sum+=n; return;
                }
            
            }
        l[i].ani.push_back({a,n}); return;
        }
    
    }
    l.push_back({p,{{a,n}}});return;
}


int main(){
    ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);
    int s; cin>>s;
    string a,p;
    int n;
    
    while(s--){
        cin>>a>>n>>p;    
        insert(a,n,p);
    }
    
    for(int i=0;i<l.size();i++){
        cout<<l[i].name<<":"<<l[i].ani[0].name<<" "<<l[i].ani[0].sum;
        for(int j=1;j<l[i].ani.size();j++){
            cout<<','<<l[i].ani[j].name<<" "<<l[i].ani[j].sum;
        }
        cout<<'\n';
    }
    
    

}