#sort from small to big
#from index[0], if index[1] < index[0], switch them
def select_sort(arr):
    for i in range(len(arr) - 1):
        for j in range(i + 1, len(arr)):
            smallest = arr[i]
            if arr[j] >= smallest:
                pass
            else:
                arr[i], arr[j] = arr[j], smallest
    return arr

print(select_sort([2, 9, 1, 8]))