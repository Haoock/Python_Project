
# def findRepeatNumber(self, nums: List[int]) -> int:
#     # 数组中任意重复数字
#     # 方法一：排序之后遍历,遇到第一个重复元素返回该元素之后结束！
#
#     nums.sort()
#     n = len(nums)
#     for i in range(n - 1):
#         if nums[i] == nums[i + 1]:
#             return nums[i]


def findRepeatNumber2(nums):
    # 原地置换（0将数组对应为哈希表）如果数组中不存在重复元素，那么应该下标与数字对应（长度为n的数组，其中数字的范围都在0到n-1范围内）
    for i in range(len(nums)):
        if nums[i] != i:  # 如果遇到下标i与nums[i]不一样，那么就要把这个nums[i]换到它应该去的下标下面。
            if nums[i] == nums[nums[i]]:  # 如果那么下标下面已经被占了，那么就找到了重复，结束就好了！
                return nums[i]
            else:
                nums[nums[i]], nums[i] = nums[i], nums[nums[i]]


nums = [1, 2, 3, 2]
findRepeatNumber2(nums)
