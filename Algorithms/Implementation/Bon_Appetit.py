n, k = input().strip().split(" ")
n, k = int(n), int(k)
c = [int(c_temp) for c_temp in input().strip().split(" ")]
b_charged = int(input())

b_actual = (sum(c) - c[k]) / 2
if b_actual == b_charged:
    print ("Bon Appetit")
else:
    print (int(b_charged - b_actual))