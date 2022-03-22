'''
785. 判断二分图

输入：graph = [[1,2,3],[0,2],[0,1,3],[0,2]]
输出：false
'''

class Solution:
    def __init__(self):
        # 记录是否符合二分图性质
        self.ok = True
        # 记录图中节点的颜色，true 和 false是两种不同的颜色
        self.color = []
        # 记录节点是否被访问过
        self.visited = []

    # 主函数，输入邻接表，判断是否是二分图 
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        self.color = [False] * n
        self.visited = [False] * n
        # 因为图不一定是联通的，可能有多个子图，所以要把每个节点都遍历一遍
        for i in range(n):
            if not self.visited[i]:
                self.traverse(graph, i)
        return self.ok
    # dfs 遍历
    def traverse(self, graph, v):
        # 已经确定不是二分图，直接返回
        if not self.ok:
            return
        self.visited[v] = True
        for w in graph[v]:
            # 相邻节点没有被访问过
            # 应该将 w 和 v 涂上不同的颜色
            if not self.visited[w]:
                self.color[w] = not self.color[v]
                # 继续遍历
                self.traverse(graph, w)
            # 相邻节点已经被访问过，根据 w 和 v颜色判断是否为二分
            else:
                # 颜色相同，不是二分
                if self.color[w] == self.color[v]:
                    self.ok = False