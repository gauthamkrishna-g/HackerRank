#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    int t;
    cin >> t;
    for (int x=0; x<t; x++) {
        int n, a, b;
        cin >> n >> a >> b;
        long int numbers[n];
        for (int i=0; i<n; i++) {
            numbers[i] = a*(n-1-i) + b*i;
            //cout << numbers[i] << " ";
        }
        sort(numbers, numbers+n);
        for (int i=0; i<n; i++) {
            while (i < n-1 && numbers[i] == numbers[i+1])
                i++;
            cout << numbers[i] << " ";
        }
        cout << "\n";
    }
    return 0;
}
