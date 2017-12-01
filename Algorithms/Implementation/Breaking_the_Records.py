n = int(input().strip())
score = list(map(int, input().strip().split(' ')))

max_count = min_count = 0
max_score = min_score = score[0]
for i in range(1, len(score)):
    if score[i] > max_score:
        max_count += 1
        max_score = score[i]
    elif score[i] < min_score:
        min_count += 1
        min_score = score[i]
print (max_count, min_count)