def solve(str1, str2):
    list_idx = [i for i, ltr in enumerate(str2) if ltr == str1[0]]
    count = 0
    for idx in list_idx:
        s1_idx = 0
        s2_idx = idx
        count = 0
        while s1_idx < len(str1):
            print("1:{} 2:{}".format(str1[s1_idx], str2[s2_idx]), end = " ")
            if str1[s1_idx] == str2[s2_idx]:
                count += 1
            else:
                break
            s2_idx += 1
            s1_idx += 1
            if s2_idx == len(str2):
                s2_idx = 0
        if count == len(str2) and count == len(str1):
            return True
        print()
    #print("First round:",count)
    print()
    if count == len(str2) and count == len(str1):
        return True
    else:
        for idx in list_idx:
            s1_idx = 0
            s2_idx = idx
            count = 0
            while s1_idx < len(str1):
                print("1:{} 2:{}".format(str1[s1_idx], str2[s2_idx]), end = " ")
                if str1[s1_idx] == str2[s2_idx]:
                    count += 1
                else:
                    break
                s2_idx -= 1
                s1_idx += 1
                if s2_idx == -1:
                    s2_idx = len(str2) - 1
            print()
    #print("Second round:",count)
    if count == len(str2) and count == len(str1):
        return True
    return False

if __name__ == "__main__":
    str1 = "amazon"
    str2 = "onamaz"
    print("Result:",solve(str1, str2))

