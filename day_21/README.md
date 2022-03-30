## 动态规划玩游戏

[174. 地下城游戏](https://leetcode-cn.com/problems/dungeon-game/)

关键不在于吃最多的血瓶，而是在于如何损失最少的生命值。

dp 函数的定义：
从 grid[i][j] 到达终点（右下角）所需的最少生命值是 dp(grid, i, j)。

根据新的 dp 函数定义和 base case，我们想求 dp(0, 0)，那就应该试图通过 dp(i, j+1) 和 dp(i+1, j) 推导出 dp(i, j)，这样才能不断逼近 base case，正确进行状态转移。

```python
def calculateMinimumHP(self, dungeon: List[List[int]]):
    m = len(dungeon)
    n = len(dungeon[0])
    # 备忘录初始化为 -1
    memo = [[-1] * (n + 1) for _ in range(m + 1)]

    # 从 (i, j) 到达右下角，需要的初始血量至少是多少 
    def dp(grid, i, j):
        # base case
        if i == m - 1 and j == n - 1:
            return 1 if grid[i][j] >= 0 else -grid[i][j] + 1
        if i == m or j == n:
            return float('inf')
        # 查备忘录
        if memo[i][j] != -1: return memo[i][j]
        # 状态转移
        res = min(
            dp(grid, i + 1, j),
            dp(grid, i, j + 1)
        ) - grid[i][j]
        memo[i][j] = 1 if res <= 0 else res
        return memo[i][j]

    return dp(dungeon, 0, 0)
```