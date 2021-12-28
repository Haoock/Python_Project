def selectionSort(arr):
    for i in range(len(arr)):
        max_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] > arr[max_idx]:
                x = j
        arr[i], arr[max_idx] = arr[max_idx], arr[i]


arr = [64, 25, 12, 22, 11, 98]
selectionSort(arr)
print("排序后的数组：")
for i in range(len(arr)):
    print("%d" % arr[i], end=' ')
