'''
1109. 航班预订统计

输入：bookings = [[1,2,10],[2,3,20],[2,5,25]], n = 5
输出：[10,55,45,25,25]
解释：
航班编号        1   2   3   4   5
预订记录 1 ：   10  10
预订记录 2 ：       20  20
预订记录 3 ：       25  25  25  25
总座位数：      10  55  45  25  25
因此，answer = [10,55,45,25,25]

'''

class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        # 航班初始值都为 0
        nums = [0] * n
        # 构造差分数组
        diff = [0] * n
        # 定义累加函数
        def increment(i, j, inc):
            diff[i] += inc
            # 当 j + 1 >= len(diff) 时，表示对 nums i之后所有的值都进行处理
            if j + 1 < len(diff):
                diff[j + 1] -= inc
        # 针对每条预定记录做处理
        for book in bookings:
            # 注意本题从 1-n
            increment(book[0] - 1, book[1] - 1, book[2])
        # 赋予第一个值
        nums[0] = diff[0]
        # 还原多步操作之后的数值
        for i in range(1, len(diff)):
            nums[i] = nums[i - 1] + diff[i]
        return nums