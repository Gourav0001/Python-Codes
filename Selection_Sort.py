def selection_sort(arr):
    for i in range(len(arr)):
        min = i
        for j in range(i + 1, len(arr)):
            if arr[min] > arr[j]:
                min = j

        arr[i], arr[min] = arr[min], arr[i]
    return arr


n = int(input("Enter number of elements : "))
a = list(map(int, input("Enter the numbers : ").strip().split()))[:n]

selection_sort(a)
print("Sorted array :", selection_sort(a))
