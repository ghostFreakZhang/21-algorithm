## 动态规划设计

## 例题分析

### 最长递增子序列
[300. 最长递增子序列](https://leetcode-cn.com/problems/longest-increasing-subsequence/)

定义：dp[i] 表示以 nums[i] 这个数结尾的最长递增子序列的长度。

根据这个定义，可推出base case，dp[i]初始值为1，因为num[i]结尾的最长递增子序列起码包含自己。

由上述定义，我们最终求得结果就是dp数组中的最大值。

解题可利用数学归纳的思想：

假设我们已经知道了 dp[0..4] 的所有结果，我们如何通过这些已知结果推出 dp[5] 呢？

根据刚才我们对 dp 数组的定义，现在想求 dp[5] 的值，也就是想求以 nums[5] 为结尾的最长递增子序列。

nums[5] = 3，既然是递增子序列，我们只要找到前面那些结尾比 3 小的子序列，然后把 3 接到这些子序列末尾，就可以形成一个新的递增子序列，而且这个新的子序列长度加一。

nums[5] 前面有哪些元素小于 nums[5]？这个好算，用 for 循环比较一波就行了。

以这些元素为结尾的最长递增子序列的长度是多少？回顾一下我们对 dp 数组的定义，它记录的正是以每个元素为末尾的最长递增子序列的长度。

以我们举的例子来说，nums[0] 和 nums[4] 都是小于 nums[5] 的，然后对比 dp[0] 和 dp[4] 的值，我们让 nums[5] 和更长的递增子序列结合，得出 dp[5] = 3。

> 题解
```python
def lengthOfLIS(nums):
    # dp[i] 表示以 nums[i] 这个数结尾的最长递增子序列的长度
    dp = [1] * len(nums)
    for i in range(len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)
```