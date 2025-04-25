def solve(word1, word2):
    f_str = ""
    l_w1 = len(word1)
    l_w2 = len(word2)
    i_1 = 0
    i_2 = 0
    while i_1 < l_w1 and i_2 < l_w2:
        if i_1 == i_2:
            f_str += word1[i_1]
            i_1 += 1
        else:
            f_str += word2[i_2]
            i_2 += 1
    
    if i_1 < l_w1:
        f_str += word1[i_1:]
    elif i_2 < l_w2:
        f_str += word2[i_2:]
    return f_str

if __name__ == "__main__":
    word1 = "c"
    word2 = "pq"
    print("Result:",solve(word1, word2))