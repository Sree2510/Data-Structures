def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min = i
        for j in range(i+1, n ):
            if arr[j] <arr[min]:
                min = j
        arr[min],arr[i] = arr[i],arr[min]
    return arr

arr = [2,5,3,8,4,9]
print(selection_sort(arr))