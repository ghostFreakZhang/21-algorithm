'''
752. 打开转盘锁

输入：deadends = ["0201","0101","0102","1212","2002"], target = "0202"
输出：6
解释：
可能的移动序列为 "0000" -> "1000" -> "1100" -> "1200" -> "1201" -> "1202" -> "0202"。
注意 "0000" -> "0001" -> "0002" -> "0102" -> "0202" 这样的序列是不能解锁的，
因为当拨动到 "0102" 时这个锁就会被锁定。
'''

class Solution:
    # 当前密码 s 的第 j 位向上拨动一次
    def plusOne(self, s, j):
        sl = list(s)
        if sl[j] == '9':
            sl[j] = '0'
        else:
            sl[j] = str(int(sl[j]) + 1)
        return ''.join(sl)

    # 当前密码 s 的第 j 位向下拨动一次
    def minusOne(self, s, j):
        sl = list(s)
        if sl[j] == '0':
            sl[j] = '9'
        else:
            sl[j] = str(int(sl[j]) - 1)
        return ''.join(sl)

    def openLock(self, deadends: List[str], target: str) -> int:
        deads = set()
        for dead in deadends:
            deads.add(dead)
        visited = set()
        q = deque()
        q.append('0000')
        visited.add('0000')
        step = 0
        while q:
            size = len(q)
            for _ in range(size):
                cur = q.popleft()
                if cur in deads:
                    continue
                # 找到目标
                if cur == target:
                    return step
                # 添加相邻的节点到队列
                for i in range(4):
                    up = self.plusOne(cur, i)
                    if up not in visited:
                        q.append(up)
                        visited.add(up)
                    down = self.minusOne(cur, i)
                    if down not in visited:
                        q.append(down)
                        visited.add(down)
            # 更新步数
            step += 1
        return -1