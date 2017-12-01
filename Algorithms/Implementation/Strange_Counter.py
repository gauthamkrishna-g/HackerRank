time = int(input().strip())
time_end = 3
value_start = 3
while time_end < time:
    value_start *= 2
    time_end += value_start
count = time_end - time + 1
print (count)
