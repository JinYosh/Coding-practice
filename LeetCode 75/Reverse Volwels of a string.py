def reverseVowels(s):
    l = 0
    r = len(s) - 1
    vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
    ans_list = [c for c in s]
    l_v_found = False
    r_v_found = False
    while l < r:
        if s[l] in vowels:
            l_v_found = True
        else:
            l += 1
        
        if s[r] in vowels:
            r_v_found = True
        else:
            r -= 1

        if l_v_found and r_v_found:
            temp = ans_list[l]
            ans_list[l] = ans_list[r]
            ans_list[r] = temp
            l += 1
            r -= 1
            l_v_found = False
            r_v_found = False
    return ''.join(x for x in ans_list)

if __name__ == "__main__":
    s = "IceCreAm"
    print("Result",reverseVowels(s))

        