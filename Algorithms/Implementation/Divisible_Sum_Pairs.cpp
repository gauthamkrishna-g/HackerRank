#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

int main()  {
    int n, k, i, j, count = 0;
    cin >> n >> k;
    vector<int> a(n);
    for (int i=0; i<n; i++)  {
       cin >> a[i];
    }
    for (i=0; i<n; i++)
        for (j=i+1; j<n; j++) {
            if ((a[i]+a[j])%k == 0)
                count++;
        }
    cout << count;
    return 0;
}
