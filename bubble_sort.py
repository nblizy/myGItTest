"""冒泡排序实现（升序）。"""


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


if __name__ == "__main__":
    data = [5, 2, 9, 1, 5, 6, -3, 0]
    print("排序前:", data)
    print("排序后:", bubble_sort(data))
