n = int(input())
bucket = {}
for _ in range(n):
    num = input()
    bucket.setdefault(len(num), []).append(num)
#print (bucket)
for key in sorted(bucket):
    for val in sorted(bucket[key]):
        print (val)
