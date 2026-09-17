"""常见排序算法实现（升序）。"""


def bubble_sort(arr):
    """就地冒泡排序：相邻元素两两比较，较大者逐步"冒"到末尾。

    若某一轮没有发生交换，说明已经有序，可提前结束。
    """
    n = len(arr)
    for i in range(n - 1):
        swapped = False
        # 后 i 个元素已就位，无需再比较
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr


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
    print("冒泡排序:", bubble_sort(list(data)))
    print("快速排序:", quick_sort(data))
