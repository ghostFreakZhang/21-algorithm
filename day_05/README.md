滑动窗口框架

```python
def slide_window(s: str, t: str):
    need = dict()
    window = dict()

    left, right = 0, 0
    valid = 0

    while right < len(s):
        # c 是即将移入窗口的字符
        c = s[right]
        # 右移（增大）窗口
        right += 1
        # 进行窗口内数据的一系列更新
        pass
        
        # debug 输出位置
        print(f'window: [{left}, {right})')

        # 左侧窗口是否要收缩
        while windows needs shrink:
            # d 是将被移出窗口的字符
            d = s[left]
            # 左移（缩小）窗口
            left += 1
            # 进行窗口内数据的一系列更新
            pass
```