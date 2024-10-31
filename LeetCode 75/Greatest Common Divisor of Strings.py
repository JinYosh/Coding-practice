def solve(str1, str2):
    small = str1 if len(str1) < len(str2) else str2
    large = str2 if small == str1 else str1
    print("Small: {} | large: {}".format(small, large))
    s_i = 0
    s_str = ""
    ans_str = ""
    while s_i < len(small):
        s_str += small[s_i]
        if len(small) % len(s_str) == 0:
            l_str_notCorrect = isDivisor(s_str, large)
            s_str_notCorrect = isDivisor(s_str, small)
            if (not l_str_notCorrect) and (not s_str_notCorrect):
                ans_str = s_str
        s_i += 1
    return ans_str

def isDivisor(s_str, large):
    l_i = 0
    notCorrect = False
    while l_i < len(large):
        if l_i + len(s_str) < len(large):
            l_str = large[l_i : l_i + len(s_str)]
            if l_str != s_str:
                notCorrect = True
                break
        else:
            l_str = large[l_i:]
            if l_str != s_str:
                notCorrect = True
            break
        l_i += len(s_str)
    return notCorrect

def solve1(str1, str2):
    small = str1 if len(str1) < len(str2) else str2
    large = str2 if len(str1) < len(str2) else str1
    for i in range(len(small), 0, -1):
        s_str = small[:i]
        div_s = div_l = False
        if len(small) % len(s_str) == 0:
            div_s = isDivisor1(s_str, small)
            if (div_s) and (len(large) % len(s_str) == 0):
                div_l = isDivisor1(s_str, large)
            if div_s and div_l:
                return s_str
    return ""

def isDivisor1(s_str, str1):
    curr_i = 0
    while curr_i < len(str1):
        if curr_i + len(s_str) <= len(str1):
            l_str = str1[curr_i:curr_i + len(s_str)]
            if l_str != s_str:
                return False
        else:
            l_str = str1[curr_i:]
            if l_str != s_str:
                return False
        curr_i += len(s_str)
    return True

def solve3(str1, str2):
    small = str1 if len(str1) < len(str2) else str2
    large = str2 if len(str1) < len(str2) else str1
    
    for i in range(len(small), 0, -1):
        s_str = small[:i]
        div_s = isDivisor3(s_str, small)
        div_l = isDivisor3(s_str, large)
        if div_s and div_l:
            print(s_str)
    return ""

def isDivisor3(s_str, str1):
    if len(str1) % len(s_str) != 0:
        return False
    factor = len(str1) // len(s_str)
    temp_str = s_str * factor
    if temp_str == str1:
        return True
    return False


        

if __name__ == "__main__":
    str1 = "TAUXXTAUXXTAUXXTAUXXTAUXX"#"ABABAB"#
    str2 = "TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX"#"ABAB"#
    
    print("Result:",solve3(str1, str2))


        

