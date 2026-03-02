#include <iostream>
#include <string>
#include <algorithm>
using namespace std;
struct a{
    int m,math,s,sc,e,number,score;
    string name;
};

bool cmp(a x,a y){
    if(x.score==y.score) return x.score>y.score;
    return x.number>y.number;
}

int main(){
    int all,math,s,sc,e,m,score;
    cin>>all;
    a list1[all];
    for(int i=0;i<all;i++){
        cin>>list1[i].number>>list1[i].name;
        cin>>m>>e>>math>>s>>sc;
        score=m+e+math+s+sc;
        list1[i].m=m;
        list1[i].e=e;
        list1[i].math=math;
        list1[i].sc=sc;
        list1[i].s=s;
        list1[i].score=score;
    }
    sort(list1,list1+all,cmp);
    int rank=1,nowrank=1;
    for(int i=0;i<all;i++){
        cout<<list1[i].number<<" "<<list1[i].name<<" "<<list1[i].m<<" "<<list1[i].e<<" "<<list1[i].math<<" "<<list1[i].s<<" "<<list1[i].sc<<" "<<list1[i].score<<" ";
        if(i>0){
            if(list1[i].score==list1[i-1].score){
                cout<<rank<<"\n";
                nowrank+=1;
            }
            else{
                rank=nowrank;
                nowrank+=1;
                cout<<rank<<"\n";
            }
        }
        else{
            cout<<rank<<"\n";
            nowrank+=1;
        }
        
    }
}