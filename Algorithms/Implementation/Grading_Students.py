n = int(input().strip())
for a0 in range(n):
    grade = int(input().strip())
    mod = grade % 5
    if grade >= 38:
        if mod >= 3:
            print (grade+5-mod)
        else:
            print (grade)
    else:
        print (grade)
