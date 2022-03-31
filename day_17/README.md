## 集合划分

站在不同的视角解题，虽然结果相同，但是解法代码的逻辑完全不同，进而算法的效率也不同。

[698. 划分为k个相等的子集](https://leetcode-cn.com/problems/partition-to-k-equal-sum-subsets/)

### 站在数字的视角

以 n 个数字的视角来看，每个数字都要选择进入 k 个子集的某一个，肯定涉及到遍历。

> 递归形式遍历数组
```python
def traverse(nums, index):
    if index == len(nums):
        return
    print(nums[index])
    return traverse(nums, index + 1)
traverse(nums, 0)
```

> for 循环模式，以数字视角遍历k个子集
```python
bucket = [0] * k
# 穷举 每个数字
for i in nums:
    # 穷举每个子集
    for j in range(k):
        # 判断每个数是否进入子集
```

> 递归形式，以数字视角遍历k个子集
```python
bucket = [0] * k
# 穷举每个数字
def backtrack(nums, index):
    # base case
    if index == len(nums):
        return
    # 穷举每个桶
    for i in range(k):
        # 装进第 i 个桶
        bucket[i] += nums[index]
        # 递归穷举下一个数字的选择
        backtrack(nums, index + 1)
        # 撤销选择
        bucket[i] -= nums[index]
```

> 再将以上代码完善，不过此解法在letcode会超时
```python
# 主函数
def canPartitionKSubsets(self, nums, k):
    if k > len(nums): return False
    if sum(nums) % k != 0: return False
    
    # k 个集合，记录数字之和
    bucket = [0] * k
    # 理论上每个集合中数字之和
    target = sum(nums) // k
    # 给nums降序排列，可以使得元素更快命中剪枝的部分
    nums.sort(reverse=True)
    # 穷举
    return backtrack(nums, 0, bucket, target)

def backtrack(nums, index, bucket, target):
    # base case
    if index == len(nums):
        # 检查所有的子集和是否等于 target
        for i in bucket:
            if i != target:
                return False
        # 可平分
        return True
    for i in range(len(bucket)):
        # 剪枝，子集和过大了
        if bucket[i] + nums[index] > target:
            continue
        # 将 nums[index] 累加到 bucket[i]
        bucket[i] += nums[index]
        # 穷举下一个数字
        if backtrack(nums, index + 1, bucket, target):
            return True
        # 撤销选择
        bucket[i] -= nums[index]
    # nums[index] 装入哪个都不行
    return False
```

### 站在子集（桶）的视角

以子集的视角进行穷举，每个桶需要遍历一遍数字，决定是否把当前数字放入子集中，装满一个子集之后，要装下一个子集，直到所有子集都一样大。

> 循环思路代码
```python
# 装满所有子集
while k > 0:
    bucket = 0
    for item in nums:
        # 能放放入当前子集中
        if canAdd(bucket, item):
            bucket += item
        if bucket == target:
            # 装满一个
            k -= 1
            break
```

> 递归解法
```python
# 主函数
def canPartitionKSubsets(self, nums, k):
    if k > len(nums): return False
    if sum(nums) % k != 0: return False

    used = [False] * len(nums)
    target = sum(nums) // k
    # 第 k 个子集初始什么都没装，从 nums[0] 开始
    return backtrack(k, 0, nums, 0, used, target)

# 存储 used 数组的状态，有计算过失败的状态可以快速返回
memo = dict()

def backtrack(k, bucket, nums, start, used, target):
    # base case
    if k == 0:
        # 所有桶都被装满了，而且 nums 一定全部用完了
        return True
    state = str(used)
    if bucket == target:
        # 装满了当前桶，递归穷举下一个桶的选择
        res = backtrack(k - 1, 0, nums, 0, used, target)
        # 存入备忘录
        memo[state] = res
        return res
    
    # 如果当前状态曾今计算过，就直接返回，不要再递归穷举了
    if state in memo:
        return memo[state]

    # 从 start 开始向后探查有效的 nums[i] 装入当前桶
    for i in range(start, len(nums)):
        # 被用过了
        if used[i]:
            continue
        # 太大了
        if nums[i] + bucket > target:
            continue
        # 做选择
        used[i] = True
        bucket += nums[i]
        # 递归穷举下一个数字是否装入当前桶
        if backtrack(k, bucket, nums, i + 1, used, target):
            return True
        # 撤销选择
        used[i] = False
        bucket -= nums[i]

    # 穷举了所有数字，不能装满子集
    return False
```
