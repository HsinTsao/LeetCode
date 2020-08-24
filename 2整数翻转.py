def reverse(x: int):
    strX = str(abs(x))
    restrX = strX[::-1]
    if x < 0:
        restrX = "-" + restrX

    if ((-2)**31) <= int(restrX) < (2 ** 31):
        return int(restrX)
    else:
        return 0


if __name__ == '__main__':
    nums = -123007777777

    print(reverse(nums))