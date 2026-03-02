#include <iostream>
using namespace std;

 struct p{
        int x, y ;
    };

p chese[16][16];
char player[16],b;

int _ , r[16][4]={0}, c[16][4]={0},l1[16]={0},l2[16]={0},a;
bool bp[16] = {false};

int main(){
    ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);
    cin >> b >> a;


    for(_ = 0 ; _ < a ; _++){
        cin >> player[_];
        for(int i = 0 ; i < 4 ; i++){
            for(int j = 0 ; j < 4 ; j++){
                int b;
                cin >> b ; 
                chese[_][b].x = i ;  chese[_][b].y = j ;
            }

        }
    }

    bool bingo = false;
    char t;
    int tp;
    cin >> t ;

    while (!(bingo))
    {
        cin >> tp; cout << tp << ' ';
        for(int i = 0 ; i < a ; i++ ){
            int tr ,tc ;
            tr = chese[i][tp].x ; tc = chese[i][tp].y ;

            r[i][tr]++;
            c[i][tc]++;
            if (r[i][tr] == 4 || c[i][tc] == 4 ){bingo = true ;  bp[i] = true ; continue ;}
            if (tr == tc ){l1[i]++;}
            if (l1[i] == 4){bingo = true ;  bp[i] = true ; continue ;}
            if ((tr+tc) == 3){l2[i]++;}
            if (l2[i] == 4){bingo = true ;  bp[i] = true ; continue ;}
        }
        
    }
    
    for (int i=0; i<a; i++){
        if (bp[i]) {cout << player[i]<< ' ';}
    }



    




}