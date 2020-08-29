def KMP_algorithm(string, substring):
    """
    KMP字符串匹配的主函数
    若存在字串返回字串在字符串中开始的位置下标，或者返回-1
    """
    next = gen_next(substring)
    n = len(string)
    m = len(substring)
    i, j = 0, 0
    while i < n and j < m:
        # 从第一个字符开始匹配
        if string[i] == substring[j]:
            i += 1
            j += 1
        # 如果不匹配，且不是第一个字符，则计算出
        # 模式字符串 和 已经匹配的字符组成的字符串
        # 之间的公共最长公共前缀
        elif j != 0:
            j = next[j - 1]
        else:
            i += 1

    if j == m:
        return i - j
    else:
        return -1


def gen_next(substring):
    """
    构造临时数组next
    """
    index = 0
    m = len(substring)
    next = [0] * m
    i = 1
    while i < m:
        if substring[i] == substring[index]:
            next[i] = index + 1
            index += 1
            i += 1
        elif index != 0:
            index = next[index - 1]
        else:
            next[i] = 0
            i += 1
    return next


if __name__ == "__main__":
    string = 'abcxabcdabcdabcy'
    substring = 'abcdabcy'
    out = KMP_algorithm(string, substring)
    print(out)

