def solve(str1, str2):
    l_s1 = len(str1)
    l_s2 = len(str2)
    i_s1 = 0
    i_s2 = 0
    s_str = ""
    temp_str = ""
    while i_s1 < l_s1 and i_s2 < l_s2:
        if str1[i_s1] == str2[i_s2]:
            temp_str += str1[i_s1]
            f1_is_d = isDivisor(str1, temp_str)
            f2_is_d = isDivisor(str2, temp_str)
            if f1_is_d and f2_is_d:
                s_str = temp_str
        else:
            return ""
        i_s1 += 1
        i_s2 += 1
    return s_str

def isDivisor(word, s_str):
    l_w = len(word)
    i = len(s_str)
    last_result = False
    if s_str == word:
        return True
    if l_w % len(s_str) != 0:
        return False
    while i + len(s_str) <= l_w:
        if word[i:i+len(s_str)] == s_str:
            last_result = True
        else:
            return False
        i += len(s_str)
    return last_result

if __name__ == "__main__":
    str2 = "ABCDABCDAB"
    str1 = "ABCD"
    print("Result:",solve(str1, str2))
    