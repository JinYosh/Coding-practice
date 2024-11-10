def closeStrings(s1, s2):
    if len(s1) != len(s2):
        return False
    HM_1 = {}
    HM_2 = {}
    for ch in s1:
        if ch in HM_1.keys():
            HM_1[ch] += 1
        else:
            HM_1[ch] = 1
    for ch in s2:
        if ch in HM_2.keys():
            HM_2[ch] += 1
        else:
            HM_2[ch] = 1
    if HM_1.keys() != HM_2.keys():
        return False
    freq_1 = sorted(HM_1.values())
    freq_2 = sorted(HM_2.values())
    if freq_1 != freq_2:
        return False
    #for ch in HM_1.keys():
    #    if HM_1[ch] != HM_2[ch]:
    #        return False
    return True

if __name__ == "__main__":
    s1 = "cabbba"
    s2 = "abbccc"
    print("Result:",closeStrings(s1, s2))

    