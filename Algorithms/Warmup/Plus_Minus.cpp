#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <iomanip>
#include <algorithm>
using namespace std;


int main(){
    int n;
    float pos, neg, zer;
    cin >> n;
    vector<int> arr(n);
    for(int arr_i = 0;arr_i < n;arr_i++) {
        cin >> arr[arr_i];
        if (arr[arr_i] > 0)
            pos++;
        else if (arr[arr_i] < 0)
            neg++;
        else
            zer++;
    }
    cout.precision(6);
    cout << fixed << static_cast<double>(pos)/n << endl;
    cout << fixed << static_cast<double>(neg)/n << endl;
    cout << fixed << static_cast<double>(zer)/n << endl;
    //cout << setprecision(6) << pos/n;    
    return 0;
}

