def removeElement(nums: [int], val: int) -> int:
    l = len(nums)
    for i in range(len(nums) - 1, -1, -1):
        if nums[i] == val:
            nums.pop(i)
            l -= 1
    return l


if __name__ == '__main__':
    n = [2, 2, 3, 8, 2]
    v = 2
    print(removeElement(n, v))