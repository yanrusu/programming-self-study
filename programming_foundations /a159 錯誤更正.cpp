#include <bits/stdc++.h>
using namespace std;

int a[100][100];

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    int n;
    while( cin >> n ) {
        if( n == 0 ) return 0;
        int rsum[100] = {0} , csum[100] = {0};
        for( int i = 0 ; i < n ; i++ ) {
            for( int j = 0 ; j < n ; j++ ) {
                cin >> a[i][j];
                rsum[i] += a[i][j];
                csum[j] += a[i][j];
            }
        }
        int rcnt = 0 , ccnt = 0;
        int ci = -1 , cj = -1;
        for( int i = 0 ; i < n ; i++ ) {
            if( rsum[i] % 2 ) {
                rcnt++;
                ci = i;
            }
            if( csum[i] % 2 ) {
                ccnt++;
                cj = i;
            }
        }
        if( ( rcnt == 0 ) && ( ccnt == 0 ) ) cout << "OK\n";
        else if( ( rcnt == 1 ) && ( ccnt == 1 ) ) cout << "Change bit (" << ci + 1 << ',' << cj + 1 << ')' << endl;
        else cout << "Corrupt" << endl;
    } 
}