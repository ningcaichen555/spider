def quickSort(arr, left=None, right=None):
    left = 0 if not isinstance(left, (int, float)) else left
    right = len(arr) - 1 if not isinstance(right, (int, float)) else right
    if left < right:
        pivotIndex = partition(arr, left, right)
        quickSort(arr, left, pivotIndex - 1)
        quickSort(arr, pivotIndex + 1, right)


def partition(array, left, right):
    piovt = left
    index = piovt + 1
    i = left + 1
    while i <= right:
        if array[piovt] > array[i]:
            swap(array, index, i)
            index = index + 1
        i += 1
    swap(array, piovt, index - 1)
    return index - 1


def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


if __name__ == '__main__':
    arr = [2, 4, 1, 3, 5, 9, 7, 8, 6]
    quickSort(arr)
    print(arr)
