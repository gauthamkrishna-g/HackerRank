#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main()  {
    int tc, n, i;
    long a[1000];
    long sum=0;
    cin>>n;
    for(i=0;i<n;i++)
    {
        cin>>a[i];
        sum+=a[i];
    }
    cout<<sum;
    return 0;
}

