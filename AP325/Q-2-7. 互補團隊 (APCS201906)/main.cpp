// force
/*#include <bits/stdc++.h>
using namespace std;

int main(){
    ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);
    int n,m,ans=0;
    string x;
    vector<set<char>> tt;
    cin>>m>>n;
    for(int i=0;i<n;i++){
        cin>>x;
        set<char> tems;
        for(auto j:x) tems.insert(j);
        tt.push_back(tems);
    }
    for(int i=0;i<n;i++){
        for(int j=i+1;j<n;j++){
            bool c=0;
            for(int z=0;z<m;z++){
                char x=z+65;
                auto iy = tt[i].find(x);
                auto jy = tt[j].find(x);
                if((iy==tt[i].end()&&jy==tt[j].end())||(iy!=tt[i].end()&&jy!=tt[j].end())) c=1;
                if(c) break;
            }
            if(!c) ans++;
        }
    }
    cout<<ans<<'\n';
}
*/

// set
/*#include <bits/stdc++.h>
using namespace std;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0);cout.tie(0);
    int n,m,ans=0;
    set<int> tt;
    cin>>m>>n;
    int ff=(1<<m)-1;
    string s;
    for(int i=0;i<n;i++){
        cin>>s;
        int sl=s.length();
        int nt=0;
        for(int j=0;j<sl;j++){
            nt |= 1<<(s[j]-'A');
        }
        if(*tt.lower_bound(ff-nt)==ff-nt) ans++;
        tt.insert(nt);
    }
    cout<<ans<<'\n';
}*/

//vector

/*#include <bits/stdc++.h>
using namespace std;

int main(){
    ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);
    int n,m,ans=0;
    vector<int> tt;
    cin>>m>>n;
    int ff=(1<<m)-1;
    string s;
    for(int i=0;i<n;i++){
        cin>>s;
        int sl=s.size(),nt=0;
        for(int j=0;j<sl;j++) nt |= 1<<(s[j]-'A');
        tt.push_back(nt);
    }
    sort(tt.begin(),tt.end());
    for(int i=0;i<n;i++) if(binary_search(tt.begin(),tt.end(),ff-tt[i])) ans++;
    cout<<ans/2<<'\n';
}*/


//  array

#include <bits/stdc++.h>
using namespace std;

int main(){
    ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);
    int n,m,ans=0,tt[50001];
    cin>>m>>n;
    int ff=(1<<m)-1;
    string s;
    for(int i=0;i<n;i++){
        cin>>s;
        int sl=s.size(),nt=0;
        for(int j=0;j<sl;j++) nt |= 1<<(s[j]-'A');
        tt[i]=nt;
    }
    sort(tt,tt+n);
    for(int i=0;i<n;i++) if(binary_search(tt,tt+n,ff-tt[i])) ans++;
    cout<<ans/2<<'\n';
}