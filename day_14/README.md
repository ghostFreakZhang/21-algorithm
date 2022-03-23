## BFS 简介
BFS 的核心思想就是把一些问题抽象成图，从一个点开始，向四周开始扩散。一般来说，我们写 BFS 算法都是用「队列」这种数据结构，每次将一个节点周围的所有节点加入队列。

BFS 相对 DFS 的最主要的区别是：BFS 找到的路径一定是最短的，但代价就是空间复杂度可能比 DFS 大很多。

## 常见场景
本质就是让你在一幅「图」中找到从起点 start 到终点 target 的最近距离

## 框架
```python
from collections import deque
def BFS(start, target):
    '''
    计算从起点 start 到终点 target 的最近距离
    '''
    # 双端队列
    q = deque()
    # 避免走回头路
    visited = set()
    # 将起点加入队列
    q.append(start)
    visited.add(start)
    # 记录扩散的步数
    step = 0
    while q:
        size = len(q)
        # 将当前队列中所有节点向四周扩散
        for _ in range(size):
            cur = q.popleft()
            # 判断是否到达终点
            if cur is target:
                return step
            # 将 cur 的相邻节点加入队列
            for x in cur.adj():
                if x not in visited:
                    q.append(x)
                    visited.add(x)
        # 更新步数在这里
        step += 1

```