#def solve(A):
#    s_set = set()
#    l_seq = 0
#    t_seq = 0
#    for i in range(len(A)):
#        if A[i] in s_set:
#            s_set = set()
#            l_seq = max(t_seq, l_seq)
#            t_seq = 0
#        s_set.add(A[i])
#        t_seq += 1
#    l_seq = max(l_seq, t_seq)
#    return l_seq

def solve(A):
    seq_dict = {}
    l_seq = 0
    l = 0
    r = 0
    temp_seq = 0
    while r < len(A):
        if A[r] in seq_dict.keys():
            while l < r:
                if A[l] == A[r]:
                    temp_seq -= 1
                    l += 1
                    break
                seq_dict.pop(A[l],None)
                temp_seq -= 1
                l += 1
        seq_dict[A[r]] = 1
        temp_seq += 1
        l_seq = max(temp_seq, l_seq)
        r += 1
    return l_seq

if __name__ == "__main__":
    A = "tmmzuxt"#"dvdf"#"AAA" #"GEEKSFORGEEKS"#""#"ABCBC"
    print("Result:",solve(A))

