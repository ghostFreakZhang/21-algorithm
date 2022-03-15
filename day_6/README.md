二分搜索框架

```python
    def binary_search(nums, target):
        left = 0
        right = ...
        while ...:
            # 防止直接进行相加后溢出
            mid = left + (right - left) / 2
            if nums[mid] == target:
                ...
            elif nums[mid] > target:
                right = ...
            elif nums[mid] < target:
                left = ...
        return ...
```