n = int(input().strip())
height = [int(height_temp) for height_temp in input().strip().split(' ')]

print (height.count(max(height)))