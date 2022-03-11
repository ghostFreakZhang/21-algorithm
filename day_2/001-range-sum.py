'''
303. 区域和检索 - 数组不可变

输入：
["NumArray", "sumRange", "sumRange", "sumRange"]
[[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
输出：
[null, 1, -1, -3]
'''

# 频繁的对数组进行操作时，可以考虑下前缀和方法
# 效率更高

class NumArray:

    def __init__(self, nums: List[int]):
        # 前缀和数组值 初始化为 0, 同时注意长度加 1
        self.preSum = [0] * (len(nums) + 1)
        for index, value in enumerate(nums, 1):
            # 注意计算方式
            self.preSum[index] = nums[index - 1] + self.preSum[index - 1]

    def sumRange(self, left: int, right: int) -> int:
        # 注意索引, 计算 [left, right] 闭区间的值
        return self.preSum[right + 1] - self.preSum[left]



# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)