def solve(s, t):
    i = 0
    t_i = 0
    match_found = False
    while i < len(s):
        match_found, t_i = f_subseq(s[i], t, t_i)
        if not match_found:
            return False
        i += 1
    return True

def f_subseq(ch, t, t_i):
    match_found = False
    while t_i < len(t):
        if ch == t[t_i]:
            match_found = True
            break
        t_i += 1
    return (match_found, t_i + 1)



if __name__ == "__main__":
    s = "ab"
    t = "cbaab"
    print("Result:",solve(s, t))