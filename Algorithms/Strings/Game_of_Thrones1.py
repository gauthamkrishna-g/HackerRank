S = input()
d = {x: S.count(x) for x in set(S)}
#print (d)
d = {key: val for key, val in d.items() if val%2 != 0}
if len(d.items()) > 1:
    print ("NO")
else:
    print ("YES")