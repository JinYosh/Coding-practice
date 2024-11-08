#def compress(chars):
#    # For one group
#    HM = {}
#    unique_list = []
#    for ch in chars:
#        if ch in HM.keys():
#            HM[ch] += 1
#        else:
#            HM[ch] = 1
#            unique_list.append(ch)
#    chars.clear()
#    for ch in unique_list:
#        freq = HM[ch]
#        chars.append(ch)
#        
#        if freq > 9:
#            temp = freq
#            mul = 10 ** (len(str(temp)) -1)
#            while temp > 0:
#                rem = temp % mul
#                quo = temp // mul
#                chars.append(str(quo))
#                temp = rem
#                mul = mul // 10
#        elif freq != 1:
#            chars.append(str(freq))
#    return len(chars)

# Update the arr and return the length
def compress1(chars):
    update_count_i = -1
    i = 0
    prev_char = ""
    curr_char = ""
    freq = 0
    while i < len(chars):
        curr_char = chars[i]
        if prev_char == curr_char:
            freq += 1
            if update_count_i == -1:
                update_count_i = i
            chars.pop(i)
        else:
            if freq > 9:
                list_fill = insertList(freq)
                for num in list_fill:
                    chars.insert(update_count_i, str(num))
                    update_count_i += 1
                    i += 1
                update_count_i = -1
                prev_char = curr_char
                freq = 1
                i += 1
                continue
            elif freq > 1:
                chars.insert(update_count_i, str(freq))
                update_count_i = -1
                prev_char = curr_char
                freq = 1
                i += 2
                continue
            prev_char = curr_char
            freq = 1
            i += 1

    if freq > 9:
        list_fill = insertList(freq)
        for num in list_fill:
            chars.insert(update_count_i, str(num))
            update_count_i += 1
    elif freq > 1:
        chars.insert(i, str(freq))
    
    return len(chars) 

def insertList(num):
    list_ = []
    mul_ = 10 ** (len(str(num)) - 1)
    while mul_ > 0:
        rem = num % mul_
        quo = num // mul_
        num = rem
        mul_ = mul_ // 10
        list_.append(quo)
    return list_

def compress(chars):
    i = 0
    len_i = 0
    p_i = 0
    prev_char = ""
    curr_char = ""
    while i < len(chars):
        curr_char = chars[i]
        if prev_char == "":
            prev_char = curr_char
            len_i = i
        elif prev_char != curr_char:
            length = i - len_i
            chars[p_i] = prev_char
            p_i += 1
            if length > 1:
                str_length = str(length)
                for ch in str_length:
                    chars[p_i] = ch
                    p_i += 1
            prev_char = curr_char
            len_i = i
        i += 1

    length = i - len_i
    chars[p_i] = prev_char
    p_i += 1
    if length > 1:
        str_length = str(length)
        for ch in str_length:
            chars[p_i] = ch
            p_i += 1
    chars = chars[:p_i]
    print(chars)
    return len(chars)
    




            

    

if __name__ == "__main__":
    chars = ["o","o","o","o","o","o","o","o","o","o"]
    #chars = ["a","a","b","b","c","c","c"]
    #chars = ["a","a","b","b","c","c","c","c","c","c","c","c","c","c","c","c","d","d"]
    #chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
    print("Result:",compress(chars))
    print(chars)