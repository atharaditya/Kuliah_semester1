def bucket_sort(arr):
    # Determine maximum value in arr
    max_val = max(arr)
    # Create list of buckets
    buckets = [[] for _ in range(max_val+1)]
    # Place array elements in appropriate bucket
    for i in range(len(arr)):
        buckets[arr[i]].append(arr[i])
    # Sort individual buckets
    for i in range(len(buckets)):
        buckets[i] = sorted(buckets[i])
    # Concatenate all buckets into a single list
    sorted_arr = []
    for i in range(len(buckets)):
        for j in range(len(buckets[i])):
            sorted_arr.append(buckets[i][j])
    return sorted_arr

# example usage
arr = [3, 2, 1, 4, 5, 7, 6, 8, 9]
print(bucket_sort(arr))
# Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]