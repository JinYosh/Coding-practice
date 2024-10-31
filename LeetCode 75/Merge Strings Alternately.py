def solve(str1, str2):
    str1_i = 0
    str2_i = 0
    newStr = ""
    while str1_i < len(str1) and str2_i < len(str2):
        newStr += str1[str1_i] + str2[str2_i]
        str1_i += 1
        str2_i += 1
    if str1_i != len(str1):
        newStr += str1[str1_i:]
    elif str2_i != len(str2):
        newStr += str2[str2_i:]
    return newStr

if __name__ == "__main__":
    str1 = "ABC"
    str2 = "PQRST"
    print("Result:",solve(str1, str2))
