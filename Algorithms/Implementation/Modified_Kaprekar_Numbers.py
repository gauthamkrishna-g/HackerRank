p = int(input())
q = int(input())
count = 0
for i in range(p, q+1):
    square = str(i ** 2)
    square_len = len(square)
    if square_len == 1 and int(square) == i:
        print (i, end=' ')
        count += 1
    elif square_len > 1:
        mid = square_len // 2
        left_square = square[:mid]
        right_square = square[mid:]
        if int(left_square) + int(right_square) == i:
            print (i, end=' ')
            count += 1
if count == 0:
    print ("INVALID RANGE")
