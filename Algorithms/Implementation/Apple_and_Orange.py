s, t = input().strip().split(' ')
s, t = [int(s), int(t)]
a, b = input().strip().split(' ')
a, b = [int(a), int(b)]
m, n = input().strip().split(' ')
m, n = [int(m), int(n)]
apples = [int(apple_temp) for apple_temp in input().strip().split(' ')]
oranges = [int(orange_temp) for orange_temp in input().strip().split(' ')]

apple_count = orange_count = 0
for apple in apples:
    if s <= (a+apple) <= t:
        apple_count += 1
for orange in oranges:
    if s <= (b+orange) <= t:
        orange_count += 1
print (apple_count)
print (orange_count)
