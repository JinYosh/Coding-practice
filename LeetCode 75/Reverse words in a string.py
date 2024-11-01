def reversString(s):
    ans_list = s.split()
    l = 0
    r = len(ans_list) - 1
    while l < r:
        temp = ans_list[l]
        ans_list[l] = ans_list[r]
        ans_list[r] = temp
        l += 1
        r -= 1
    return " ".join(x for x in ans_list)

if __name__ == "__main__":
    s = "  hello world  "
    print("Result:",reversString(s))