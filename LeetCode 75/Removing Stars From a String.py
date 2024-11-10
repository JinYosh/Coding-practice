def removeStars(s):
    stack_ = []
    for ch in s:
        if ch == "*":
            if len(stack_) > 0:
                stack_.pop()
        else:
            stack_.append(ch)
    return "".join(c for c in stack_)

if __name__ == "__main__":
    s = "leet**cod*e"
    print("Result:",removeStars(s))
