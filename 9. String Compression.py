def solve(chars):
    i = 1
    e_i = 0
    prev = chars[0]
    count = 1
    while i < len(chars):
        if prev == chars[i]:
            count += 1
        else:
            if count == 1:
                chars[e_i] = prev
                e_i += 1
            elif count > 1:
                s_count = str(count)
                chars[e_i] = prev
                e_i += 1
                for k in range(len(s_count)):
                    chars[e_i] = s_count[k]
                    e_i += 1
            count = 1
            prev = chars[i]
        i += 1
    if count == 1:
        chars[e_i] = prev
        e_i += 1
    elif count > 1:
        s_count = str(count)
        chars[e_i] = prev
        e_i += 1
        for k in range(len(s_count)):
            chars[e_i] = s_count[k]
            e_i += 1

    # delete remaining elements
    arr_size = len(chars)
    for _ in range(e_i, arr_size, 1):
        chars.pop(e_i)
        
    return len(chars)



    

if __name__ == "__main__":
    chars = ["a","a","b","b","c","c","c"]
    solve(chars)
    print("Result:",chars)
