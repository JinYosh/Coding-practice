def decodeString(s):
    stack_ = []
    for ch in s: #"3[a]2[bc]"
        if ch == "]":
            numFound = False
            str_ = ""
            while len(stack_) > 0:
                char = stack_.pop()
                if char == "[":
                    # Get whole numeric value and break
                    num = 0
                    mul = 1
                    while len(stack_) > 0:
                        c = stack_.pop()
                        if len(c) > 1 or (ord(c) >= ord('a') and ord(c) <= ord('z')) or c == "[":
                            stack_.append(c)
                            break
                        elif ord(c) >= ord('0') and ord(c) <= ord('9'):
                            numFound = True
                            temp_num = int(c) * mul
                            num = temp_num + num
                            mul *= 10
                    str_ = str_ * num
                else:
                    str_ = char + str_
                if numFound:
                    print(stack_)
                    stack_.append(str_)
                    break
        else:
            stack_.append(ch)
    return "".join(c for c in stack_)

def decodeString1(s):
    stack_ = []
    for ch in s:
        if ch != "]":
            stack_.append(ch)
        else:
            str_ = ""
            while stack_[-1] != "[":
                str_ = stack_.pop() + str_
            stack_.pop()
            
            str_num = ""
            while stack_ and stack_[-1].isdigit():
                str_num = stack_.pop() + str_num
            num = int(str_num)

            stack_.append(str_ * num)
    return "".join(stack_)

if __name__ == "__main__":
    #s = "3[a]2[bc]"
    #s = "3[a2[bc]]"
    s = "3[z]2[2[y]pq4[2[jk]e1[f]]]ef"
    print("Result:",decodeString1(s))

