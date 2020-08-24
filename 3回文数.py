def isPalindrome(x: int):
    if x < 0:
        return False
    temp_x = x
    palindromeNum = 0
    while temp_x != 0:
        palindromeNum = (palindromeNum * 10) + (temp_x % 10)
        temp_x //= 10

    return palindromeNum == x


if __name__ == '__main__':
    nums = 123454321
    print(isPalindrome(nums))
