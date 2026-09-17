"""快速排序实现（升序）。"""


def quick_sort(arr):
    """返回升序新列表：选基准值，分治成"小于基准 / 等于基准 / 大于基准"三部分。"""
    if len(arr) <= 1:
        return list(arr)
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    mid = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + mid + quick_sort(right)


if __name__ == "__main__":
    data = [5, 2, 9, 1, 5, 6, -3, 0]
    print("排序前:", data)
    print("排序后:", quick_sort(data))
