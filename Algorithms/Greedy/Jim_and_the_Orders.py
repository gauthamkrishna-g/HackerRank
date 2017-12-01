n = int(input())
receive_times = []
for i in range(n):
    t, d = input().split(' ')
    t, d = int(t), int(d)
    receive_times.append(t+d)
#print (sorted(enumerate(receive_times), key=lambda x: x[1]))
receive_orders = [i[0]+1 for i in sorted(enumerate(receive_times), key=lambda x: x[1])]
print (*receive_orders)
