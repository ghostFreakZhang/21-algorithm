## 编辑距离
[72. 编辑距离](https://leetcode-cn.com/problems/edit-distance/)

思路：

base case 是 i 走完 s1 或 j 走完 s2，可以直接返回另一个字符串剩下的长度。

对于每对儿字符 s1[i] 和 s2[j]，可以有四种操作：

```python
if s1[i] == s2[j]:
    # 啥都不做，skip
    # i, j同时向前移动
    pass
else:
    # 三选一：
    # 如何选择？全试一遍，哪个操作最后得到的编辑距离最小，就选谁。
    插入(insert)
    删除(delete)
    替换(replace)
```

> 暴力递归实现代码

时间超时

```python
def minDistance(s1, s2):
    # 定义：dp(i, j) 返回 s1[0..i] 和 s2[0..j] 的最小编辑距离
    def dp(i, j):
        # base case
        if i == -1: return j + 1
        if j == -1: return i + 1

        if s1[i] == s2[j]:
            # 啥都不做
            return dp(i - 1, j - 1)
        else:
            return min(
                dp(i, j - 1) + 1, # 插入
                dp(i - 1, j) + 1, # 删除
                dp(i - 1, j - 1) + 1 # 替换
            )
    # i, j 初始化指向最后一个索引
    return dp(len(s1) - 1, len(s2) - 1)
```

> dp table 解法

dp table 是二维数组，dp[..][0] 和 dp[0][..] 对应 base case，dp[i][j] 的含义和之前的 dp 函数类似，存储 s1[0..i] 和 s2[0..j] 的最小编辑距离。

```python
def minDistance(s1, s2):
    m = len(s1)
    n = len(s2)
    # 定义：s1[0..i] 和 s2[0..j] 的最小编辑距离是 dp[i+1][j+1]
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    # base case
    for i in range(m):
        dp[i][0] = i
    for j in range(n):
        dp[0][j] = j
    # 自底向上求解
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(
                    dp[i - 1][j] + 1,
                    dp[i][j - 1] + 1,
                    dp[i - 1][j - 1] + 1
                )
    # 储存着整个 s1 和 s2 的最小编辑距离
    return dp[m][n]
```