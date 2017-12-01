from itertools import combinations

n,m = input().strip().split(' ')
n,m = int(n),int(m)
topics = []
for i in range(n):
    topic = input()
    topics.append(topic)
persons = list(combinations(range(n), 2))
sums = []
#for i, j in zip(range(n-1), range(1, n)):
for i, j in persons:
    total_sum = str(int(topics[i]) + int(topics[j]))
    two_person_sum = len(total_sum) - total_sum.count('0')
    '''while k < m:
        #if int(topics[i][k]) | int(topics[j][k]) != 0:
        two_person_sum += (int(topics[i][k]) | int(topics[j][k]) != 0)
        k += 1'''
    sums.append(two_person_sum)
#print (sums)
print (max(sums))
print (sums.count(max(sums)))