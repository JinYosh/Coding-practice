def solve(s):
    vowels_list = []
    vowels = {'a','A','e','E','i','I','o','O','u','U'}
    for c in s:
        if c in vowels:
            vowels_list.append(c)
    vowels_list.reverse()
    i = 0
    v_i = 0
    ans_str = ""
    while i < len(s):
        if s[i] in vowels:
            ans_str += vowels_list[v_i]
            v_i += 1
        else:
            ans_str += s[i]
        i += 1
    return ans_str

if __name__ == "__main__":
    s = "IceCreAm"
    print("Result:",solve(s))