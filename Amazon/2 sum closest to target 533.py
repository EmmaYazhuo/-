# Given array nums = [-1, 2, 1, -4], and target = 4.
#The minimum difference is 1. (4 - (2 + 1) = 1).
#Do it in O(nlogn) time complexity.

import sys
def twoSumClosest(nums, target):
    minV = sys.maxsize
    nums = sorted(nums)
    # print(nums)
    left, right = 0, len(nums)-1
    while left < right:
        if nums[left] + nums[right] < target:
            minV = min(minV, target - nums[left] - nums[right])
            left += 1
        else:
            minV = min(minV, nums[left] + nums[right] - target)
            right -= 1
    return minV

target = 20
input = ([[1,8],[3,9], [2,15]],  [[1,8], [2,11], [3,12]] )
output = [[1, 3], [3, 2]]
# def ON2(nums, target):
#     #枚举所有可能避免重复出现的可能？

def main():
    nums = [-1, 2, 1, -4]
    target = 4
    print(twoSumClosest(nums, target))

main()