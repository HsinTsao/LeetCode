def twoSum(nums: [int], target: int):
    l = len(nums)
    for i in range(l):
        for j in range(i+1,l):
            if nums[i] + nums[j] == target:
                return [i,j]


if __name__ == '__main__':
    nums = [2,7,11,15]
    target = 9
    print(twoSum(nums,target))