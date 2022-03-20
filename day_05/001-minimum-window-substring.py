'''
76. 最小覆盖子串

给你一个字符串 s 、一个字符串 t 。返回 s 中涵盖 t 所有字符的最小子串。
如果 s 中不存在涵盖 t 所有字符的子串，则返回空字符串 "" 。

对于 t 中重复字符，我们寻找的子字符串中该字符数量必须不少于 t 中该字符数量。
如果 s 中存在这样的子串，我们保证它是唯一的答案。

输入：s = "ADOBECODEBANC", t = "ABC"
输出："BANC"
'''
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # 目标需要的内容
        need = dict()
        # 当前窗口内的内容
        windows = dict()
        # 计算 need 值
        for c in t:
            need[c] = need.setdefault(c, 0) + 1
        # 初始化左右指针
        left, right = 0, 0
        # 左闭右开区间, 初始情况下没有任何元素
        # 代表满足 need 条件的字符个数, valid 和 need.size 相同时，找到覆盖子串T
        valid = 0
        # 记录最下覆盖字串的起始索引以及长度
        start = 0
        len_ = len(s) + 1
        # 注意结束条件
        while right < len(s):
            # 即将移入窗口字符
            c = s[right]
            # 右移窗口
            right += 1
            # 更新数据
            if c in need:
                windows[c] = windows.setdefault(c, 0) + 1
                if need[c] == windows[c]:
                    valid += 1
            # 判断左侧要收缩
            while valid == len(need):
                # 更新最小覆盖子串
                if right - left < len_:
                    start = left
                    len_ = right - left
                # 即将移除的字符
                d = s[left]
                # 左移窗口
                left += 1
                # 更新窗口数据
                if d in need:
                    if need[d] == windows[d]:
                        valid -= 1
                    windows[d] -= 1
        # 返回最小覆盖子串
        return '' if len_ == len(s) + 1 else s[start:start+len_]