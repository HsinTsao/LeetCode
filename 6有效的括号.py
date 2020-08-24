def isValid(s: str):
    dic = {'{': '}',
           '[': ']',
           '(': ')'}

    stack = []
    for c in s:
        # 遇到左括号
        if c in dic:
            stack.append(c)
        # 否则如果遇到右括号
        elif not stack:
            return False
        elif dic[stack.pop()] != c:
            return False

    return len(stack) == 0


if __name__ == '__main__':
    str2 = '({{[]}})'
    str1 = '(){}{})()'
    print(isValid(str1))
    print(isValid(str2))


