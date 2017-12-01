def check_beautiful(s):
    if s[0] == '0':
        return False
    
    for s_i in range(1, len(s)//2+1):
        i, curr_num = s_i, int(s[:s_i])
        result = [curr_num]
        while i < len(s):
            num_plus_one = curr_num + 1
            num_plus_one_len = len(str(num_plus_one))
            next_num = int(s[i:i+num_plus_one_len])
            if str(next_num)[0] == '0' or next_num != num_plus_one:
                result = []
                break
            result.append(next_num)
            i, curr_num = i + num_plus_one_len, next_num
    
        if len(result) > 1:
            return result[0]
        
q = int(input().strip())
for _ in range(q):
    s = input().strip()
    first_num = check_beautiful(s)
    if first_num:
        print ("YES", str(first_num))
    else:
        print ("NO")