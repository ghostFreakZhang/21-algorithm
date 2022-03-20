'''
48. 旋转图像

输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
输出：[[7,4,1],[8,5,2],[9,6,3]]

顺时针旋转二维数组 90度
'''

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # 获取行列值
        n = len(matrix)
        for i in range(n):
            # 左上到右下的对角线
            # 沿左对角线镜像对称矩阵，注意 j 的初始值，避免取重复值，被对称两次
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        # 将每行元素进行反转
        for index, item in enumerate(matrix):
            matrix[index] = item[::-1]
    
    def rotate_2(self, matrix: List[List[int]]) -> None:
        '''
        逆时针旋转 90 度
        '''
        n = len(matrix)
        for i in range(n):
            # 左下到右上角的对角线对称, j 的值为 0 -- n-i-1
            for j in range(n - i):
                # 注意对称 交换的索引值
                matrix[i][j], matrix[n - j - 1][n - i -1] = matrix[n - j - 1][n - i -1], matrix[i][j]

        for index, item in enumerate(matrix):
            matrix[index] = item[::-1]   