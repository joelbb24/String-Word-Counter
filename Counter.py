
def splitString(s):
    split_value = []
    tmp = ''
    for c in s:
        if c == ' ':
            split_value.append(tmp)
            tmp = ''
        else:
            tmp += c
    if tmp:
        split_value.append(tmp)

    return split_value


sentence = input("Enter Input: ")
res = splitString(sentence)
print(res)
