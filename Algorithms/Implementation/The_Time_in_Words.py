h = int(input())
m = int(input())
d = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 15: "quarter", 16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen", 20: "twenty"}
for i in range(1, 10):
    d[20+i] = "twenty " + str(d[i])
d[30] = "half"
d[45] = "quarter"
#print (d)
if h == 12 and m > 30:
    if m == 45:
        print (d[45], "to one")
    elif m == 59:
        print (d[1], "minute to one")
    else:        
        print (d[60-m], "minutes to one")
elif m <= 30:
    if m == 0:
        print (d[h], "o' clock")
    elif m == 1:
        print (d[m], "minute past one")
    elif m == 15 or m == 30:
        print (d[m], "past", d[h])
    else:        
        print (d[m], "minutes past", d[h])
elif m > 30:
    if m == 59:
        print (d[1], "minute to", d[h+1])
    elif m == 45:
        print (d[45], "to", d[h+1])        
    else:
        print (d[60-m], "minutes to", d[h+1])
