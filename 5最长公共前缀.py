def longestCommonPrefix(strs):
    str = strs[0]
    res = ''
    for temp in str:
        res += temp
        for s in strs:
            if s.find(res, 0, len(s)) == -1:
                return res[:-1]

    return res


if __name__ == '__main__':
    strlist = ["flower","flow","fli"]
    print(longestCommonPrefix(strlist))
