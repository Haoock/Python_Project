# 插入排序
def insertionSort(arr):
    for i in range(len(arr)):
        temp = arr[i]
        for j in range(i):
            if temp > arr[j]:
                temp2 = arr[j]
                arr[j] = temp
                temp = temp2
        arr[i] = temp


'''
def insertionSort(arr):
    for i in range(1, len(arr)):

        key = arr[i]

        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
'''

arr = [12, 11, 13, 5, 6, 19]
insertionSort(arr)
print("排序后的数组为：")
for i in range(len(arr)):
    print("%d" % arr[i], end=' ')
