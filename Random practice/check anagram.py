def isAnagramIterative(str1, str2):
    if len(str1) != len(str2):
        return False
    str1_list = [ch for ch in str1]
    str2_list = [ch for ch in str2]
    
    for i in range(len(str1_list)):
        chFound = False
        for j in range(len(str2_list)):
            if str1_list[i] == str2_list[j]:
                str2_list[j] = None
                chFound = True
        if not chFound:
            return False
    return True

def isAnagramHM(str1, str2):
    str1_HM = {}
    str2_HM = {}
    if len(str1) != len(str2):
        return False
    for ch in str1:
        if ch in str1_HM:
            str1_HM[ch] += 1
        else:
            str1_HM[ch] = 1
    for ch in str2:
        if ch in str2_HM:
            str2_HM[ch] += 1
        else:
            str2_HM[ch] = 1

    for ch in str1_HM.keys():
        if str1_HM[ch] != str2_HM[ch]:
            return False
    return True

def isAnagramAlphabets(str1, str2):
    if len(str1) != len(str2):
        return False
    aphabets_list_1 = [0] * ((ord('z') - ord('a')) + 1) 
    aphabets_list_2 = [0] * ((ord('z') - ord('a')) + 1)
    for i in range(len(str1)):
        aphabets_list_1[ord(str1[i]) - ord('z')] += 1
        aphabets_list_2[ord(str2[i]) - ord('z')] += 1
    for i in range((ord('z') - ord('a')) + 1):
        if aphabets_list_1[i] != aphabets_list_2[i]:
            return False
    return True

    

if __name__ == "__main__":
    str1 = "abc"
    str2 = "cba"
    print("Result:",isAnagramAlphabets(str1, str2)) 
