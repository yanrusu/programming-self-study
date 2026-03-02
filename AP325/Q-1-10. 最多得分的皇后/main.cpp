#include <bits/stdc++.h>
using namespace std;
int s[12][12],ans=0;

// 遞迴 皇后位置 目前列 總列 分數
void q(int p[],int n,int k,int sc){
    // .終止條件
    if(k>=n){
         // 比較
        if (sc>ans) ans=sc;
        return;
    }

// 不放
    p[k]=-1;
    q(p,n,k+1,sc);
    bool vaild[12];
    for(int i=0;i<12;i++) vaild[i]=true;
    
// 遍歷
// 確認可放位置
    for(int j=0;j<k;j++){
        // 如果無 continue
        if(p[j]==-1) continue;
         // 左右
        vaild[p[j]] = false;
        // 下對角
        int i= k-j+p[j];
        if(i<n) vaild[i]=0;
        //上對角
        i=j-k+p[j];
        if(i>=0) vaild[i]=0;
    }
// 嘗試
    for(int j=0;j<n;j++){
         // 可放
        if(vaild[j]){
            p[k]=j;
            // 呼叫
            q(p,n,k+1,sc+s[k][j]);
        }
    }
    
    return;

}

// 主程式 
int main(){
    ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);
    int n;
    cin>>n;
    for(int i=0;i<n;i++){
        for(int j=0;j<n;j++){
            cin>>s[i][j];
        }
    }
    int p[12];
    q(p,n,0,0);
    
    cout<<ans<<'\n';
    
    // 呼叫
    // 輸出最終值
}
