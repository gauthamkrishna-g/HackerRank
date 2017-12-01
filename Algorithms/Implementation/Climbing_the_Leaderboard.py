n = int(input().strip())
scores = [int(scores_temp) for scores_temp in input().strip().split(' ')]
m = int(input().strip())
alice = [int(alice_temp) for alice_temp in input().strip().split(' ')]

scores = sorted(set(scores), reverse=True)
for a_score in alice:
    while scores and a_score >= scores[-1]:
        scores.pop()
    print (len(scores) + 1)        
