#include <bits/stdc++.h>
using namespace std;
//全域
int a[14][14];
vector<int> mi;
void cut(int n1, int n2, int m1, int m2, int sum){
    //終止條件 相減 = 1
    if(m2-m1<=1 || n2-n1<=1){
        mi.push_back(sum);
        return ;
    }
    //切上
    int su=0;
    for(int j=m1;j<m2;j++) su+=a[n1][j];
    if(m2-m1-su>su) cut(n1+1,n2,m1,m2,su+sum);
    else cut(n1+1,n2,m1,m2,m2-m1-su+sum);
    //切下
    su=0;
    for(int j=m1;j<m2;j++) su+=a[n2-1][j];
    if(m2-m1-su>su) cut(n1,n2-1,m1,m2,sum+su);
    else cut(n1,n2-1,m1,m2,m2-m1-su+sum);
    //切左
    su=0;
    for(int i=n1;i<n2;i++) su+=a[i][m1];
    if(n2-n1-su>su) cut(n1,n2,m1+1,m2,su+sum);
    else cut(n1,n2,m1+1,m2,n2-n1-su+sum);
    //切右
    su=0;
    for(int i=n1;i<n2;i++) su+=a[i][m2-1];
    if(n2-n1-su>su) cut(n1,n2,m1,m2-1,sum+su);
    else cut(n1,n2,m1,m2-1,sum+n2-n1-su);
    
    return;
}

int main(){
    ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);
    int n,m;
    cin>>n>>m;
    //輸入
    for(int i=0;i<n;i++){
        for(int j=0;j<m;j++){
            cin>>a[i][j];
        }
    }
    cut(0,n,0,m,0);
    cout<<*min_element(mi.begin(),mi.end());
}





/*
   bool valid[4];
    int best;
    // 對四邊計算
    //上
    int sum=0;
    for(int j=m1;j<m2;j++) sum+=a[n1][j];
    if(m2-m1-sum>sum) best=sum;
    else best=m2-m1-sum;
    
    valid[0]=true;
    //下
    sum=0;
    for(int j=m1;j<m2;j++) sum+=a[n2-1][j];
    if(m2-m1-sum>sum){
        if(sum<best){
            best=sum;
            valid[1]=true;
        }
        else valid[1]=false;
    }
    else{
        if(m2-m1-sum<best){
            best=m2-m1-sum;
            valid[1]=true;
        }
        else valid[1]=false;
    }
    //左
    sum=0;
    for(int i=n1;i<n2;i++) sum+=a[i][m1]
    if(n2-n1-sum>sum){
        if(sum<best){
            best=sum;
            valid[2]=true;
        }
        else valid[2]=false
        
    }
    else{
        if(n2-n1-sum<best){
            best=n2-n1-sum;
            valid[2]=true;
        }
        else valid[2]
    }
    // 右
    sum=0
    for(int i=n1;i<n2;i++) sum+=a[i][m2-1];
    if(n2-n1-sum>sum){
        if(sum<best){
            best=sum;
            valid[3]=true;
        }
        else valid[3]=false
        
    }
    else{
        if(n2-n1-sum<best){
            best=n2-n1-sum;
            valid[2]=true;
        }
        else valid[2]
    }
    //判斷最小邊 更新範圍
    for(int i=0;i<)
    
    //再傳
    */