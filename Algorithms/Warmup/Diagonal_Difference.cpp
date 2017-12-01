#include <math.h>
#include <iostream>
using namespace std;

int main(){
    int n;
    cin >> n;
    int a[n][n], i, j, x = 0, y = 0;
    for(i=0; i<n; i++) {
       for(j=0; j<n; j++) {
          cin >> a[i][j];
       }
    }
    for(i=0; i<n; i++)
        x += a[i][i];
    for(i=0, j=n-1; i<n, j>=0; i++, j--)
        y += a[i][j];
    cout << abs(x-y);
    return 0;
}
		