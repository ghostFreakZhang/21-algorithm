'''
59. 螺旋矩阵 II

给你一个正整数 n ，生成一个包含 1 到 n2 所有元素，
且元素按顺时针顺序螺旋排列的 n x n 正方形矩阵 matrix 。

输入：n = 3
输出：[[1,2,3],[8,9,4],[7,6,5]]
'''

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        # 需要被填入矩阵的数字
        index = 1
        # 上下左右边界
        up_bound, down_bound = 0, n - 1
        left_bound, right_bound = 0, n - 1
        # 初始化二维数组
        res = [[0 for _ in range(n)] for _ in range(n)]

        # 注意循环截至条件，小于等于 n * n
        while index <= n * n:
            # 从左往右遍历，增大上边界
            if up_bound <= down_bound:
                for i in range(left_bound, right_bound + 1):
                    res[up_bound][i] = index
                    index += 1
                up_bound += 1
            # 从上往下遍历，减小右边界
            if left_bound <= right_bound:
                for j in range(up_bound, down_bound + 1):
                    res[j][right_bound] = index
                    index += 1
                right_bound -= 1
            # 从右往左遍历，减小下边界
            if up_bound <= down_bound:
                for i in range(right_bound, left_bound - 1, -1):
                    res[down_bound][i] = index
                    index += 1
                down_bound -= 1
            # 从下往上遍历，增大左边界
            if left_bound <= right_bound:
                for j in range(down_bound, up_bound - 1, -1):
                    res[j][left_bound] = index
                    index += 1
                left_bound += 1
        return res