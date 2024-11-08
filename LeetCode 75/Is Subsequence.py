def isSubsequence(s, t):
    s_i = 0
    t_i = 0
    while s_i < len(s):
        found = False
        while t_i < len(t):
            if s[s_i] == t[t_i]:
                found = True
                t_i += 1
                break
            t_i += 1
        if not found:
            return False
        s_i += 1
    return True

if __name__ == "__main__":
    s = "axc"
    t = "ahbgdc"
    print("Result:",isSubsequence(s, t))
            