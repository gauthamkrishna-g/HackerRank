#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <iterator>
using namespace std;

int main() {
    int n, k, i, x=0, y=0;
    cin >> n >> k;
    long long int sum_impl=0, sum_nimpl=0, sum_loss=0, sum=0, l[n], len;
    int t[n];
    for (i=0; i<n; i++) {
        cin >> l[i] >> t[i];
        sum += l[i];
    }
    //cout << sum << "\n";
    for (i=0; i<n; i++) {
        if (t[i] == 1)
            x++;
    }
    long long int impl[x];
    x=0;
    for (i=0; i<n; i++) {
        if (t[i] == 1)  {
            impl[x] = l[i];
            sum_impl += impl[x];
            //index[x] = i;
            x++;
        }
        else if (t[i] == 0)
            sum_nimpl += l[i];
    }
    len = sizeof(impl)/sizeof(impl[0]);
    //cout << x << "\n";
    sort(impl, impl+x);
    //cout << len << " " << sum_impl << " "<< sum_nimpl;
    if (k<x)
        y = k;
    else
        y = len;
    for (i=0; i<y; i++) {
        if (x > 0)
            sum_loss += impl[x-i-1];
        else
            sum_loss = 0;          
    }
    sum_loss *= 2;
    sum = sum_nimpl - sum_impl + sum_loss;
    //cout << " " << sum_loss << " ";
    cout << sum;
    //int a = *min_element(l, l+n);
    //int b = distance(l.begin(), a);
    //int b = a - l.begin();
    //cout << a << "\n";
    //if (t[i] == 1)    {}
    //for (i=0; i<n; i++)
      //  cout << l[i] << " "<< t[i] << "\n";
    return 0;
}
