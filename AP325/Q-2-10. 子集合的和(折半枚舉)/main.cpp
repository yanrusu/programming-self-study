/*#include <bits/stdc++.h>
using namespace std;
typedef long long LL;
LL sa[1<<19],sb[1<<19];
LL s(LL s[], int len, LL a[]){
    LL k=0;
    for(int i=0;i<len;i++){
        for(LL j=0;j<k;j++){
            s[k+j]=s[j]+a[i];
        }
        s[k+k]=a[i];
        k+=k+1;
    }
    return k;
}
int main(){
    LL P,a[20],b[20];
    int n;
    cin>>n>>P;
    int a_len=n/2,b_len=n-a_len;
    for(int i=0;i<a_len;i++) cin>>a[i];
    for(int i=0;i<b_len;i++) cin>>b[i];
    LL sa_len=s(sa,a_len,a);
    LL sb_len=s(sb,b_len,b);
    sort(sa,sa+sa_len);
    sort(sb,sb+sb_len);
    LL aa = lower_bound(sa,sa+sa_len,P)-sa;
    LL ba = lower_bound(sb,sb+sb_len,P)-sb;
    LL ans=0;
    if(sa[aa]<=P) ans=sa[aa];
    if(sa_len>=2&&sa[aa-1]<=P&&sa[aa-1]>ans) ans=sa[aa-1];
    if(sb[ba]<=P&&sb[ba]>ans) ans=sb[ba];
    if(sb_len>=2&&sb[ba-1]<=P&&sb[ba-1]>ans) ans=sb[ba-1];
    for(LL i=0;i<aa;i++){
        LL tem=sa[i];
        LL sear=lower_bound(sb,sb+sb_len,P-tem)-sb;
        if(tem+sb[sear]<=P&&tem+sb[sear]>ans) ans=tem+sb[sear];
        if(sb_len>=2&&tem+sb[sear-1]<=P&&tem+sb[sear-1]>ans) ans=tem+sb[sear-1];
    }
    cout<<ans<<'\n';
    
    
    return 0;
    
}*/

/*#include <bits/stdc++.h>
using namespace std;
typedef long long LL;
LL sa[1<<19],sb[1<<19];
LL s(LL s[], int len, LL a[]){
    LL k=0;
    for(int i=0;i<len;i++){
        for(LL j=0;j<k;j++){
            s[k+j]=s[j]+a[i];
        }
        s[k+k]=a[i];
        k+=k+1;
    }
    return k;
}
int main(){
    ios::sync_with_stdio(0);cin.tie(0);cout.tie(0);
    LL P,a[20],b[20];
    int n;
    cin>>n>>P;
    int a_len=n/2,b_len=n-a_len;
    for(int i=0;i<a_len;i++) cin>>a[i];
    for(int i=0;i<b_len;i++) cin>>b[i];
    LL sa_len=s(sa,a_len,a);
    LL sb_len=s(sb,b_len,b);
    sort(sa,sa+sa_len);
    sort(sb,sb+sb_len);
    LL aa = lower_bound(sa,sa+sa_len,P)-sa;
    LL ba = lower_bound(sb,sb+sb_len,P)-sb;
    LL ans=0;
    if(sa[aa]<=P) ans=sa[aa];
    else if(aa-1<sa_len) ans=sa[aa-1];
    if(sb[ba]<=P&&sb[ba]>ans) ans=sb[ba];
    else if(ba-1<sb_len&&sb[ba-1]>ans) ans=sb[ba-1];
    for(LL i=0;i<aa;i++){
        LL tem=sa[i];
        LL sear=lower_bound(sb,sb+sb_len,P-tem)-sb;
        if(tem+sb[sear]<=P&&tem+sb[sear]>ans) ans=tem+sb[sear];
        else if(sear-1<sb_len&&tem+sb[sear-1]>ans) ans=tem+sb[sear-1];
    }
    cout<<ans<<'\n';
}*/

#include <bits/stdc++.h>
using namespace std;
typedef long long LL;
LL sa[1<<19],sb[1<<19];
LL s(LL s[], int len, LL a[]){
    LL k=0;
    for(int i=0;i<len;i++){
        for(LL j=0;j<k;j++){
            s[k+j]=s[j]+a[i];
        }
        s[k+k]=a[i];
        k+=k+1;
    }
    return k;
}
int main(){
    ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);
    LL P,a[20],b[20];
    int n;
    cin>>n>>P;
    int a_len=n/2,b_len=n-a_len;
    for(int i=0;i<a_len;i++) cin>>a[i];
    for(int i=0;i<b_len;i++) cin>>b[i];
    LL sa_len=s(sa,a_len,a);
    LL sb_len=s(sb,b_len,b);
    sort(sa,sa+sa_len);
    sort(sb,sb+sb_len);
    LL aa = upper_bound(sa,sa+sa_len,P)-sa-1;
    LL ba = upper_bound(sb,sb+sb_len,P)-sb-1;
    LL ans=0;
    if(sa[aa]<=P) ans=sa[aa];
    if(sb[ba]<=P&&sb[ba]>ans) ans=sb[ba];
    for(LL i=0;i<aa;i++){
        LL tem=sa[i];
        LL sear=upper_bound(sb,sb+sb_len,P-tem)-sb-1;
        if(tem+sb[sear]<=P&&tem+sb[sear]>ans) ans=tem+sb[sear];
    }
    cout<<ans<<'\n';
}