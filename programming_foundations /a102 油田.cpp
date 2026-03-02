#include <iostream>
using namespace std;
int n,m;
char oil[101][101]={'*'};

void dfs(int x,int y){
    oil[x][y]='*';
    int arr[8][2]={{1,0},{0,1},{-1,0},{0,-1},{1,1},{-1,-1},{-1,1},{1,-1}};
    for(int i=0;i<8;i++){
        if(x+arr[i][0]>=0&&y+arr[i][1]>=0&&y+arr[i][1]<m&&x+arr[i][0]<n){
            if(oil[x+arr[i][0]][y+arr[i][1]]=='@'){
                dfs(x+arr[i][0],y+arr[i][1]);
            }
        }
    }
    return;
}

int main(){
    ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);
    while(cin>>n>>m&&n&&m){
        int ans=0;
        for(int i=0;i<n;i++){
            for(int j=0;j<m;j++){
                cin>>oil[i][j];
            }
        }
        for(int i=0;i<n;i++){
            for(int j=0;j<m;j++){
                if(oil[i][j]=='@'){dfs(i,j);ans++;}
            }
        }
        cout<<ans<<'\n';
        
    }
}