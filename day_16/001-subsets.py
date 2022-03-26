'''
78. 子集

给你一个整数数组 nums ，数组中的元素 互不相同 。返回该数组所有可能的子集（幂集）。
解集 不能 包含重复的子集。你可以按 任意顺序 返回解集

输入：nums = [1,2,3]
输出：[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
'''

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # 存储结果
        res = []
        # 存储路径
        track = []

        # 回溯核心代码
        def backtrace(nums, start):
            # 前序位置，每个节点值都是一个子集
            res.append(list(track))

            for i in range(start, len(nums)):
                # 做选择
                track.append(nums[i])
                # start 控制树枝的遍历，避免重复的子集
                backtrace(nums, i + 1)
                # 撤销选择
                track.pop()

        backtrace(nums, 0)
        return res