#include <bits/stdc++.h>
using namespace std;
#define ll long long

struct two{
    ll value;
    ll idx;
};

bool cmp(two a,two b){
    return a.value>b.value;
}

two a[1<<19];
ll ans[1<<19] , indi=2;

void r(ll left, ll right, ll water, ll input){
    if((right-left)==1){
        ans[left] = water; // input+1; 
        return;
    }
    //剩一個水槽 水槽高等於剩下的水
    while(a[indi].idx>=right||a[indi].idx<=left){ // <= >= < >
        indi++;
    }
    
    ll h = a[indi].value; // 溢位
    ll rl = right-left;
    //水能夠填滿全部都是最高的兩端
    if(water>=rl*h){
        ll allhigh = water/rl;
        for(int i=left;i<right;i++){
            ans[i]=allhigh;
        }
        return;
    }
    ll hidx = a[indi].idx;
    if(hidx>input){//左邊
        ll hl = hidx - left;
        if(water>(hl)*h){ // 會越過 水會超出ㄧ端，遞迴另一邊，這邊確定水高是最高的那個
            for(int i=left;i<hidx;i++){
                ans[i]=h;
            }
            r(hidx,right,water-(hl*h),hidx); //水只夠填滿一端，把另一邊丟掉
            return;    
        }
        else{
            r(left,hidx,water,input);
            return;
        }
        
    }
    else{
        ll rh = right - hidx;
        if(water>rh*h){
            for(int i=hidx;i<right;i++){
                ans[i]=h;
            }
            r(left,hidx,water-rh*h,hidx);// hidx-1+1
            return;
        }
        else{
            r(hidx,right,water,input);
            return;
        }
    }
    //水只夠填滿一端，把另一邊丟掉
    //水會超出ㄧ端，遞迴另一邊，這邊確定水高是最高的那個
    return;
}

int main(){
    ll n,i;
    ll w;
    cin>>n>>i>>w;
    for(int i=0;i<n;i++){
        cin>>a[i].value;
        a[i].idx=i;
    }
    sort(a,a+n,cmp);
    r(0,n-1,w,i);

    for(int i=0;i<n-1;i++){
        cout<<ans[i]<<" ";
    }
}

/*
correct
#include <bits/stdc++.h>
using namespace std;
#define ll long long

struct two{
    ll value;
    ll idx;
};

bool cmp(two a,two b){
    return a.value>b.value;
}

two a[1<<19];
ll ans[1<<19] , indi=2;

void r(ll left, ll right, ll water, ll input){
    if((right-left)==1){
        ans[input] = water;  
        return;
    }
    
    while(a[indi].idx>=right||a[indi].idx<=left){
        indi++;
    }
    
    ll h = a[indi].value , rl = right-left;
    if(water>=rl*h){
        ll allhigh = water/rl;
        for(int i=left;i<right;i++){
            ans[i]=allhigh;
        }
        return;
    }
    ll hidx = a[indi].idx;
    
    if(hidx>input){
        ll hl = hidx - left;
        if(water>(hl)*h){ 
            for(int i=left;i<hidx;i++){
                ans[i]=h;
            }
            r(hidx,right,water-(hl*h),hidx); 
            return;    
        }
        else{
            r(left,hidx,water,input);
            return;
        }
        
    }
    else{
        ll rh = right - hidx;
        if(water>rh*h){
            for(int i=hidx;i<right;i++){
                ans[i]=h;
            }
            r(left,hidx,water-rh*h,hidx);
            return;
        }
        else{
            r(hidx,right,water,input);
            return;
        }
    }
    return;
}

int main(){
    ll n,i;
    ll w;
    cin>>n>>i>>w;
    for(int i=0;i<n;i++){
        cin>>a[i].value;
        a[i].idx=i;
    }
    sort(a,a+n,cmp);
    r(0,n-1,w,i);

    for(int i=0;i<n-1;i++){
        cout<<ans[i]<<" ";
    }
}*/

