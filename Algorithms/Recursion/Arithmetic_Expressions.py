def calc(i, res, exp):
    global N, arr
    if res % 101 == 0:
        return exp + '*' + '*'.join((map(str, arr[i:]))) if i < N else exp
    if i == N:
        return ''
    sub_exp = calc(i+1, res+arr[i], exp + '+' + str(arr[i]))
    if sub_exp != '':
        return sub_exp
    sub_exp = calc(i+1, res-arr[i], exp + '-' + str(arr[i]))
    if sub_exp != '':
        return sub_exp
    sub_exp = calc(i+1, res*arr[i], exp + '*' + str(arr[i]))
    if sub_exp != '':
        return sub_exp
    return ''

N = int(input())
arr = [int(arr_temp) for arr_temp in input().split(' ')]
print (calc(1, arr[0], str(arr[0])))
