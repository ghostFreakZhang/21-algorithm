'''
54. 螺旋矩阵
给你一个 m 行 n 列的矩阵 matrix ，请按照 顺时针螺旋顺序 ，返回矩阵中的所有元素。

输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
输出：[1,2,3,6,9,8,7,4,5]

注意边界值设定，以及遍历结束条件
'''

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        row = len(matrix)
        col = len(matrix[0])
        # 设定四个方向的边界值
        up_bound, down_bound = 0, row - 1
        left_bound, right_bound = 0, col -1
        # 结果数组
        res = []
        # 遍历完数组条件
        while len(res) < row * col:
            if up_bound <= down_bound:
                # 在顶部，从左往右遍历
                for i in range(left_bound, right_bound + 1):
                    res.append(matrix[up_bound][i])
                # 上边界 加1
                up_bound += 1
            if left_bound <= right_bound:
                # 在右侧，从上往下遍历
                for j in range(up_bound, down_bound + 1):
                    res.append(matrix[j][right_bound])
                # 右边界 减1
                right_bound -= 1
            if up_bound <= down_bound:
                # 在下侧，从右往左遍历
                for i in range(right_bound, left_bound - 1, -1):
                    res.append(matrix[down_bound][i])
                # 下边界 减1
                down_bound -= 1
            if left_bound <= right_bound:
                # 在左侧，从下往上遍历
                for j in range(down_bound, up_bound - 1, -1):
                    res.append(matrix[j][left_bound])
                # 左边界 减1
                left_bound += 1
        return res