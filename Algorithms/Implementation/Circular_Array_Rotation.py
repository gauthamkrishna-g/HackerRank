n,k = input().strip().split(' ')
n,k = [int(n),int(k)]
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

counts = [0] * k
for number in arr:
    counts[number % k] += 1

count = min(counts[0], 1)
for i in range(1, k//2+1):
    if i != k - i:
        count += max(counts[i], counts[k-i])
if k % 2 == 0: 
    count += 1

print(count)

'''#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    int n, k, q, i, m;
    cin >> n >> k >> q;
    int a[n];
    for (i=0; i<n; i++)
        cin >> a[(i+k)%n];    
    for (i=0; i<q; i++)  {
        cin >> m;
        cout << a[m] << "\n";
    }
    return 0;
} '''
