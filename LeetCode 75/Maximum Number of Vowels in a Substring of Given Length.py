def maxNumVowels(s, k):
    vowels = "aeiou"
    max_vow = 0
    vow = 0
    for i in range(k):
        if s[i] in vowels:
            vow += 1
    max_vow = vow
    l = 0
    for i in range(k, len(s), 1):
        if s[l] in vowels:
            vow -= 1
        if s[i] in vowels:
            vow += 1
        max_vow = max(vow, max_vow)
        l += 1
    return max_vow

if __name__ == "__main__":
    s = "aeiou"
    k = 2
    print("Result:",maxNumVowels(s, k))
