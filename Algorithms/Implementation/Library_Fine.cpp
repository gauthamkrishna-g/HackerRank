#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int main(){
    int dr, mr, yr;
    cin >> dr >> mr >> yr;
    int de, me, ye;
    cin >> de >> me >> ye;
    if ((yr < ye) || (yr == ye && mr < me) || (yr == ye && mr == me && dr <= de))   {
        cout << "0";
    }
    else if (dr > de && mr == me && yr == ye)
        cout << (dr-de)*15;
    else if (mr > me && yr == ye)             
        cout << (mr-me)*500;
    else
        cout << "10000";
    return 0;
}
