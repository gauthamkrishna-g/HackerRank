chaps, k = input().strip().split(' ')
chaps, k = int(chaps), int(k)
probs_per_chap = [int(t_temp) for t_temp in input().strip().split(' ')]
special = 0
page = 1
prob = 1
chap = 0
while chap < chaps:
    if prob <= page and page <= min(prob+k-1, probs_per_chap[chap]):
        special += 1
    page += 1
    prob += k
    if prob > probs_per_chap[chap]:
        chap += 1
        prob = 1
print (special)
