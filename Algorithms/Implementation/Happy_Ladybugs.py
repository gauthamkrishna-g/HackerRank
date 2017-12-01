def happiness(n, b):
    if b.count("_") == 0 and unhappiness_string_only(b):
        return False
    for i in b:
        if i != "_" and b.count(i) == 1:
            return False
    return True        

def unhappiness_string_only(b):
    if len(b) == 1:
        return True
    for i in set(b):
        i_count = b.count(i)
        if i * i_count != b[b.index(i):b.index(i)+i_count]:
            return True
    return False            

Q = int(input())
for _ in range(Q):
    n = int(input())
    b = input()
    print ("YES" if happiness(n, b) == True else "NO")
