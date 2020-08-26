# def removeDuplicates(nums: []) -> int:
#     l = len(nums)
#     for idx in range(0, l):
#         if idx < l:
#             for i in range(l - 1, idx-1, -1):
#                 if nums[idx] == nums[i] and i != idx:
#                     nums.pop(i)
#                     print(i,idx)
#                     print(nums[idx], nums[i])
#                     l -= 1
#     return l

def removeDuplicates(nums):
    i = 0
    j = 1
    while j < len(nums):
        if nums[i] == nums[j]:
            j += 1
        else:
            i += 1
            nums[i] = nums[j]
    return(i + 1)


if __name__ == '__main__':
    s = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    print(removeDuplicates(s))
