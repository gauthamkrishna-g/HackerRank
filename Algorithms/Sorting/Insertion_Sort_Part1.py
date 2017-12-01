size = int(input())
arr = [arr_temp for arr_temp in input().strip().split(' ')]
i = size - 1
temp = arr[i]
while i > 0 and arr[i-1] > temp:
    arr[i] = arr[i-1]
    i -= 1
    print (' '.join(arr))        
arr[i] = temp
print (' '.join(arr))

'''#include <iostream>
#include <algorithm>
using namespace std;

int main(void) {
    int size, i, j, k, pos, temp;
    cin >> size;
    int arr[size];
    for(i=0; i<size; i++)
        cin >> arr[i];  
    pos = size-1;
    temp = arr[pos];
    for(j=0; j<size-pos; j++) {
        if(arr[pos-1] > temp) {
            arr[pos] = arr[pos-1];
            pos--;
        }
        else
            arr[pos] = temp;
        for(i=0; i<size; i++)   {
            cout << arr[i] << " ";
        }
        cout << "\n";
    }
    return 0;
}'''
