n = int(input().strip())
calories = list(map(int, input().strip().split(' ')))

calories.sort(reverse=True)
miles = 0
for i in range(len(calories)):
    miles += (calories[i] * (2 ** i))
print (miles)