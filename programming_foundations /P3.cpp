#include <iostream>
using namespace std;
#define int long long

pair<int, int> path(int N) {
    int left = 0;
    int right = 0;

    while (N > 1) {
        if (N % 2 == 0) {  
            left++;
        } else { 
            right++;
        }
        N /= 2; 
    }

    return make_pair(left, right);
}

signed main() {
    int a;
    cin >> a;

    for (int i = 0; i < a; ++i) {
        int n;
        cin >> n;
        pair<int, int> ans = path(n);
        cout << ans.first << " " << ans.second << endl;
    }
}
