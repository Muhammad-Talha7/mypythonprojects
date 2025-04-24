def binary_search_recursive(arr, target, low, high):
    if low > high:
        return -1
    mid = (low + high) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, high)
    else:
        return binary_search_recursive(arr, target, low, mid - 1)

sorted_list = [1, 3, 5, 7, 9, 11, 13, 15]
target_value = 7
result = binary_search_recursive(sorted_list, target_value, 0, len(sorted_list) - 1)
if result != -1:
    print(f"Target found at index {result}")
else:
    print("Target not found")