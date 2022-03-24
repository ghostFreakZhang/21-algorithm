'''
46. 全排列

给定一个不含重复数字的数组 nums ，返回其 所有可能的全排列 。你可以 按任意顺序 返回答案。

输入：nums = [1,2,3]
输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
'''

'''
import itertools
print(list(map(list, itertools.permutations([1,2,3], 3))))
'''

'''
回溯算法，核心在于做选择和取消选择。
在递归之前做出选择，在递归之后撤销刚才的选择。
'''
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # 记录结果
        res = []
        # 记录路径
        track = []
        # 路径中的元素会被标记为True,避免重复使用
        used = [False] * len(nums)

        def backtrace(nums, track, used):
            # 结束条件
            if len(track) == len(nums):
                res.append(list(track))
                return
            for i in range(len(nums)):
                # 排除不合法的已经使用过的选择
                if used[i]:
                    continue
                # 进行选择
                track.append(nums[i])
                used[i] = True
                # 进入下一层选择
                backtrace(nums, track, used)
                # 取消选择
                track.pop()
                used[i] = False

        backtrace(nums, track, used)
        return res