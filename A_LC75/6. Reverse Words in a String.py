def solve(s):
    s_list = s.split()
    s_list.reverse()
    ans_str = " ".join(s_list)
    return ans_str

if __name__ == "__main__":
    s = "  hello world "
    print("Result:",solve(s))