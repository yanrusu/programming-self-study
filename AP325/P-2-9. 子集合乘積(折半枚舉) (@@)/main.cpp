/*#include <bits/stdc++.h>
using namespace std;

long long P,sb[1<<19],sa[1<<19];
long long num[1<<19],subid=1;
void sub(long long ms[], int s[], int len, long long &k, int nlen, long long value,bool empty){
    if(nlen>=len){
        if(empty){
            ms[k]=value;
            k++;
            return;
        }
        return;
        }
    
    sub(ms,s,len,k,nlen+1,(s[nlen]*value)%P,true);
    sub(ms,s,len,k,nlen+1,value,empty);
    return;
}

long long ex(long long x, long long y){
    long long t=1,xi=x;
    while(y>0){
        if(y&1) t=(t*xi)%P;
        xi=(xi*xi)%P;
        y>>=1;
    }
    return t;
}

int main(){
    int n,a[19],b[19];
    cin>>n>>P;
    int alen=n/2,blen=n-(n/2);
    for(int i=0;i<alen;i++) cin>>a[i];
    for(int i=0;i<blen;i++) cin>>b[i];
    long long ka=0,kb=0;
    sub(sa,a,alen,ka,0,1,false);
    sub(sb,b,blen,kb,0,1,false);
    num[0]=1;
    sort(sb,sb+kb);
    for(int i=1;i<kb;i++){
        if(sb[i]!=sb[i-1]){
            sb[subid]=sb[i];
            num[subid]=1;
            subid++;
        }
        else num[subid-1]++;
    }
    cout<<subid;
    long long ans=0;
    if(sb[0]==1) ans=num[0]%P;
    else ans=0;
    for(int i=0;i<ka;i++){
        if(sa[i]==1){
            ans=(ans+1)%P;
        }
        long long taget=ex(sa[i],P-2);
        int it=lower_bound(sb,sb+subid,taget)-sb;
        if(it<subid&&sb[it]==taget){
            ans=(ans+num[it])%P;
        }
        
    }
    cout<<ans;
}*/

