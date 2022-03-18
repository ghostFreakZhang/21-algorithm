'''
146. LRU 缓存
请你设计并实现一个满足  LRU (最近最少使用) 缓存 约束的数据结构。
实现 LRUCache 类：
LRUCache(int capacity) 以 正整数 作为容量 capacity 初始化 LRU 缓存
int get(int key) 如果关键字 key 存在于缓存中，则返回关键字的值，否则返回 -1 。
void put(int key, int value) 如果关键字 key 已经存在，则变更其数据值 value ；如果不存在，则向缓存中插入该组 key-value 。如果插入操作导致关键字数量超过 capacity ，则应该 逐出 最久未使用的关键字。
函数 get 和 put 必须以 O(1) 的平均时间复杂度运行。

'''
class LRUCache:

    def __init__(self, capacity: int):
        self.maxsize = capacity
        # 建立有序字典, 模仿哈希链表
        self.lrucache = collections.OrderedDict()

    def get(self, key: int) -> int:
        # 值在缓存中, 移动到字典尾部, 尾部为最近访问
        if key in self.lrucache:
            self.lrucache.move_to_end(key)
        return self.lrucache.get(key, -1)

    def put(self, key: int, value: int) -> None:
        # 若存在, 则删掉, 重新在尾部添加
        if key in self.lrucache:
            del self.lrucache[key]
        # 在尾部添加
        self.lrucache[key] = value
        # 超出存储空间时, 从头部移除, 头部为最久未访问
        if len(self.lrucache) > self.maxsize:
            self.lrucache.popitem(last = False)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)