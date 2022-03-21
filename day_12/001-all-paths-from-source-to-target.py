'''
797. 所有可能的路径

给你一个有 n 个节点的 有向无环图（DAG），请你找出所有从节点 0 到节点 n-1 的路径并输出（不要求按特定顺序）
graph[i] 是一个从节点 i 可以访问的所有节点的列表（即从节点 i 到节点 graph[i][j]存在一条有向边）。

输入：graph = [[1,2],[3],[3],[]]
输出：[[0,1,3],[0,2,3]]
解释：有两条路径 0 -> 1 -> 3 和 0 -> 2 -> 3
'''

'''
以 0 为起点遍历图，同时记录遍历过的路径，当遍历到终点时将路径记录下来即可。
主要是要熟悉图的遍历，该题给的是图的邻接表表示，可以直接使用遍历。
'''

class Solution:
    def __init__(self):
        # 记录所有路径
        self.res = []
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        # 维护递归过程中经过的路径
        path = []

        # 图的遍历
        def traverse(graph, s, path):
            # 添加节点 s 的路径
            path.append(s)
            n = len(graph)
            # 到达终点
            if s == n - 1:
                self.res.append(list(path))
                path.pop()
                return
            # 递归每个相邻节点
            for v in graph[s]:
                traverse(graph, v, path)
            # 从路径中移除节点 s
            path.pop()
        
        traverse(graph, 0, path)
        return self.res