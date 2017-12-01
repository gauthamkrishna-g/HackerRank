#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    int t;
    cin >> t;
    for (int a=0; a<t; a++) {
        long long pris=0, sweets=0, id=0, i, id_count;
        cin >> pris >> sweets >> id;
 
        id_count = sweets % pris;
        id_count += id - 1;
        id_count = id_count % pris;
        if (id_count == 0)
            id_count = pris;    
                           
        cout << id_count << "\n";
        //cout << pris;
        }
    return 0;
}