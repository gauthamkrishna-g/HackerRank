n, d = input().strip().split(' ')
n, d = int(n), int(d)
#a = [int(a_temp) for a_temp in input().strip().split(' ')]
a = list(map(int, input().split()))
a_ji = set(x-d for x in a)
a_kj = set(x-(2*d) for x in a)
a = set(a)
print (len(a_ji & a_kj & a))
