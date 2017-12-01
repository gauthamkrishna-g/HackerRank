V = int(input())
n = int(input())
ar = [int(ar_temp) for ar_temp in input().strip().split(' ')]
if V in ar:
    print (ar.index(V))