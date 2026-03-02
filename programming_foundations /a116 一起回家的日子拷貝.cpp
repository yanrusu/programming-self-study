#include <iostream>

using namespace std;

int month[12]={31,28,31,30,31,30,31,31,30,31,30,31};

void year(int y){
    if((y%4==0 && y%100!=0)||(y%400==0)) month[1]=29;
    else month[1]=28;
}


int main(){
    ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);
    int a; cin>>a;
    int n[a],lcm=0,l=1;
    for(int i = 0; i<a;i++) cin>>n[i];
    
    int y,m,d;
    char s;
    int i;
    cin>>y>>s>>m>>s>>d;
    bool c=true;
    while(c){
        lcm=n[0]*l;
        for(i=1;i<a;i++){
            if(lcm%n[i]!=0){
                break;
            }
        }
        if(i<a) l++;
        else break;
    }
    
    year(y);
    
    while(lcm){
        lcm--;d++;
        
        if(d>month[m-1]){
            d=1;
            m+=1;
        }
        if(m>12){
            m=1;
            y+=1;
            year(y);
        }
    }
    
    cout<<y<<s;
    if(m<10) cout<<0<<m<<s;
    else cout<<m<<s;
    if(d<10) cout<<0<<d;
    else cout<<d;
    
    cout<<'\n';
}
