'''
380. O(1) 时间插入、删除和获取随机元素

实现RandomizedSet 类：

RandomizedSet() 初始化 RandomizedSet 对象
bool insert(int val) 当元素 val 不存在时，向集合中插入该项，并返回 true ；否则，返回 false 。
bool remove(int val) 当元素 val 存在时，从集合中移除该项，并返回 true ；否则，返回 false 。
int getRandom() 随机返回现有集合中的一项（测试用例保证调用此方法时集合中至少存在一个元素）。每个元素应该有 相同的概率 被返回。
你必须实现类的所有函数，并满足每个函数的 平均 时间复杂度为 O(1) 。


输入
["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"]
[[], [1], [2], [2], [], [1], [2], []]
输出
[null, true, false, true, 2, true, false, 2]
'''

'''
利用哈希表和数组结合的方式解题
'''

class RandomizedSet:
    
    def __init__(self):
        # 数组存储元素的值
        self.nums = []
        # 利用哈希表记录元素值对应的索引,便于快速进行交换
        self.val_to_index = dict()

    def insert(self, val: int) -> bool:
        # 值已存在,不插入
        if val in self.val_to_index:
            return False
        # 值不存在,插入到数组尾部,并更新索引值
        self.val_to_index[val] = len(self.nums)
        self.nums.append(val)
        return True

    def remove(self, val: int) -> bool:
        # 值不存在,不用移除
        if val not in self.val_to_index:
            return False
        # 取到值的索引
        index = self.val_to_index[val]
        # 更新最后一个元素的索引
        self.val_to_index[self.nums[-1]] = index
        # 交换最后一个元素和要移除的值
        self.nums[index], self.nums[-1] = self.nums[-1], self.nums[index]
        # 删除最后一个元素,以及删除哈希表对应记录
        del self.val_to_index[self.nums.pop()]
        return True

    def getRandom(self) -> int:
        return self.nums[random.randint(0, len(self.nums)-1)]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()