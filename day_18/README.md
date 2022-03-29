## 动态规划套路
求解动态规划的核心问题是穷举。
1、动态规划问题存在「重叠子问题」,如果暴力穷举的话效率会极其低下,所以需要「备忘录」或者「DP table」来优化穷举过程,避免不必要的计算。

2、动态规划问题一定会具备「最优子结构」,才能通过子问题的最值得到原问题的最值。

3、虽然动态规划的核心思想就是穷举求最值,但是问题可以千变万化,穷举所有可行解其实并不是一件容易的事,只有列出正确的「状态转移方程」,才能正确地穷举。

## 例题分析

### 斐波那契数列
[509. 斐波那契数](https://leetcode-cn.com/problems/fibonacci-number/)

> 一般递归版本：
```python
def fib(N):
    if N == 1 or N == 2: return N
    return fib(N - 1) + fib(N - 2)
```
自己画出递归树后可发现, 存在大量的重复计算,比如 f(18) 被计算了两次,而且你可以看到,以 f(18) 为根的这个递归树体量巨大,多算一遍,会耗费巨大的时间。更何况,还不止 f(18) 这一个节点被重复计算,所以这个算法及其低效。
> 带备忘录的自顶向下递归版本
```python
def fib(N):
    memo = [0] * (N + 1)
    def helper(memo, n):
        # base case
        if n == 0 or n == 1: return n
        # 计算过就不再计算
        if memo[n] != 0: return memo[n]
        # 没计算过就记录一下
        memo[n] = helper(memo, n - 1) + helper(memo, n - 2)
        return memo[n]
    # 进行带备忘录的递归
    return helper(memo, N)
```
耗时的原因是重复计算,那么可以造一个「备忘录」,每次算出某个子问题的答案后别急着返回,先记到「备忘录」里再返回；每次遇到一个子问题先去「备忘录」里查一查,如果发现之前已经解决过这个问题了,直接把答案拿出来用,不要再耗时去计算了。

「自顶向下」？含义是从上向下延伸,都是从一个规模较大的原问题比如说 f(20),向下逐渐分解规模,直到 f(1) 和 f(2) 这两个 base case,然后逐层返回答案。

> 自底向上递推求解

「自底向上」？从最底下、最简单、问题规模最小、已知结果的 f(1) 和 f(2)（base case）开始往上推,直到推到我们想要的答案 f(20)。这就是「递推」的思路,这也是动态规划一般都脱离了递归,而是由循环迭代完成计算的原因。

``` python
def fib(N):
    if N == 0: return 0
    dp = [0] * (N + 1)
    # base case
    dp[0] = 0
    dp[1] = 1
    # 状态转移
    for i in range(1, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[N]
```

> 进一步优化空间

仔细观察状态转移方程, 当前状态只和之前的两个状态有关, 其实并不需要那么长的一个dp table来存储所有状态, 只想办法存储之前的状态即可。

```python
def fib(N):
    if n == 0 or n == 1: return n
    # 两个变量 分别代表 dp[i - 1] 和 dp[i - 2]
    dp_i_1 = 1
    dp_i_2 = 0
    for i in range(1, n + 1):
        # dp[i] = dp[i - 1] + dp[i - 2]
        dp_i = dp_i_1 + dp_i_2
        dp_i_2 = dp_i_1
        dp_i_1 = dp_i
    return dp_i_1
```
如果我们发现每次状态转移只需要 DP table 中的一部分, 那么可以尝试缩小 DP table 的大小, 只记录必要的数据, 从而降低空间复杂度。

### 凑零钱问题

[322. 零钱兑换](https://leetcode-cn.com/problems/coin-change/)

> 自顶向下递归法

递归会超时

```python
def coinChange(coins, amount):
    # 要凑出金额 n, 至少要 dp(coins, n)个硬币
    def dp(coins, amount):
        # base case
        if amount == 0: return 0
        if amount < 0: return -1
        res = float('inf')
        for coin in coins:
            # 计算子问题结果
            sub_problem = dp(coins, amount - coin)
            # 子问题无解则跳过
            if sub_problem == -1: continue
            # 在子问题中选择最优解, 然后加1
            res = min(res, sub_problem + 1)
        return -1 if res == float('inf') else res
    return dp(coins, amount)
```

> 带备忘录的递归

```python
def coinChange(coins, amount):
    memo = [-666] * (amount + 1)
    # 要凑出金额 n, 至少要 dp(coins, n)个硬币
    def dp(coins, amount):
        # base case
        if amount == 0: return 0
        if amount < 0: return -1
        # 查备忘录
        if memo[amount] != -666:
            return memo[amount]

        res = float('inf')
        for coin in coins:
            # 计算子问题结果
            sub_problem = dp(coins, amount - coin)
            # 子问题无解则跳过
            if sub_problem == -1: continue
            # 在子问题中选择最优解, 然后加1
            res = min(res, sub_problem + 1)
        memo[amount] =  -1 if res == float('inf') else res
        return memo[amount]
    return dp(coins, amount)
```

> dp 数组的迭代解法

dp 数组的定义：当目标金额为 i 时，至少需要 dp[i] 枚硬币凑出。

```python
def coinChange(coins, amount):
    dp = [amount + 1] * (amount + 1)
    # base case
    dp[0] = 0
    # 外层 for 循环在遍历所有状态的所有取值
    for i in range(len(dp)):
        # 内层 for 循环在求所有选择的最小值
        for coin in coins:
            # 子问题无解，跳过
            if i - coin < 0:
                continue
            dp[i] = min(dp[i], 1 + dp[i - coin])
    return -1 if dp[amount] == amount + 1 else dp[amount]
```