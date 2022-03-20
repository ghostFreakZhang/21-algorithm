'''
1094. 拼车

输入：trips = [[2,1,5],[3,3,7]], capacity = 4
输出：false
'''
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        # 站点取值范围为0-1000，初始化 1001
        nums = [0] * 1001
        # 构造差分数组
        diff = [0] * 1001
        
        # 每次变动的处理函数
        def increment(i, j, inc):
            diff[i] += inc
            if j + 1 < len(nums):
                diff[j + 1] -= inc

        for trip in trips:
            # 乘客在 trip[2] 已经下车
            # 在车上的区间要 减去 1
            increment(trip[1], trip[2] -1, trip[0])

        # 计算最终在每个站点时车上的人数
        nums[0] = diff[0]
        for i in range(1, len(diff)):
            nums[i] = nums[i - 1] + diff[i]

        # 每个站点都不能超载
        for n in nums:
            if n > capacity:
                return False
        return True