def partition(array, low, high):
    pivot = array[high]
    i = low - 1
    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
            (array[i], array[j]) = (array[j], array[i])
    (array[i + 1], array[high]) = (array[high], array[i + 1])
    return i + 1

def quickSort(array, low, high):
    if low < high:
        pi = partition(array, low, high)
        quickSort(array, low, pi - 1)
        quickSort(array, pi + 1, high)

size = int(input("Enter the size of the array: "))
arr = []
for i in range(size):
    num = int(input("Enter element " + str(i + 1) + ": "))
    arr.append(num)

quickSort(arr, 0, size - 1)

print('Sorted Array in Ascending Order:')
print(arr)

n = len(arr)
print("Given array is")
for i in range(n):
    print("%d" % arr[i], end=" ")
