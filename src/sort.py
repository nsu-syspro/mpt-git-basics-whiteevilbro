arr = [40, 4, 20, 10, 30, 6, 10]

# selection sort:
for i in range(len(arr) - 1):
    min = i
    for j in range(i + 1, len(arr)):
        print("comparing {} and {}".format(arr[j], arr[min]))
        if arr[j] < arr[min]:
            min = j
    arr[i], arr[min] = arr[min], arr[i]

print(arr)
