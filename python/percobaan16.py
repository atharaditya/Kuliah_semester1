#perocobaan 14.14 algoritma comb sort
#program comb sort dengan python
def comb_sort(arr):
    n = len(arr)
    gap = n
    shrink = 1.3
    sorted = False
    while not sorted:
        gap = int(gap / shrink)
        if gap > 1:
            sorted = False
        else:
            gap = 1
            sorted = True
        i = 0
        while i + gap < n:
            if arr[i] > arr[i + gap]:
                arr[i], arr[i + gap] = arr[i + gap], arr[i]
                sorted = False
            i += 1
    return arr

# menguji algoritma comb sort
arr = [5, 3, 8, 6, 1, 9, 2, 7, 4]
print('Algoritma Comb Sort')
print('Data sebelum di urutkan',arr)
sorted_arr = comb_sort(arr)
print('Data sebelum di urutkan',sorted_arr)

print()

#percobaan 14.15 algoritma bucket sort
#program bucket sort dengan python
def bucket_sort(array, num_buckets=10):
    # Create a list of empty buckets
    buckets = [[] for _ in range(num_buckets)]

    # Distribute the elements of the array into the buckets
    for elem in array:
        buckets[int(elem * num_buckets)].append(elem)

    # Sort the elements within each bucket
    for i in range(num_buckets):
        buckets[i] = sorted(buckets[i])

    # Concatenate the sorted buckets to get the sorted array
    sorted_array = []
    for bucket in buckets:
        sorted_array.extend(bucket)

    return sorted_array

array = [0.3, 0.1, 0.2, 0.4, 0.5]
print('Algoritma Bucket Sort')
print('Data sebelum diurutkan',array)
print('Data setelah diurutkan',bucket_sort(array))

print()

#percobaan 14.16 algoritma radix sort
#program radix sort dengan python
def radix_sort(arr):
    # Find the maximum number to know number of digits
    max_number = max(arr)

    # Do Counting Sort for every digit. Note that instead
    # of passing digit number, exp is passed. exp is 10^i
    # where i is current digit number
    exp = 1
    while max_number/exp > 0:
        counting_sort_by_digit(arr, exp)
        exp *= 10

def counting_sort_by_digit(arr, exp):
    # Create a bucket for each digit (0-9)
    bucket = [[] for _ in range(10)]

    # Place each element in the appropriate bucket based on its digit
    for number in arr:
        bucket[(number//exp) % 10].append(number)

    # Concatenate the buckets back into the original array
    arr[:] = [number for bucket in bucket for number in bucket]
    
# Test the function
unsorted = [170, 45, 75, 90, 802, 24, 2, 66]
print('Algoritma Radix Sort')
print('Data sebelum diurutkan',unsorted)
radix_sort(unsorted)
print('Data setelah diurutkan',unsorted)

print()

#percobaan 14.17 algoritma radix sort 2
#program radix sort 2 dengan python
# Radix sort 2 in Python
# Using Counting Sort to sort the elements in the basis of significant places
def countingSort(array, place):
    size = len(array)
    output = [0] * size
    count = [0] * 10

    # Calculate count of elements
    for i in range(0, size):
        index = array[i] // place
        count[index % 10] += 1

    # Calculate cumulative count
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Place the elements in sorted order
    i = size - 1
    while i >= 0:
        index = array[i] // place
        output[count[index % 10] - 1] = array[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(0, size):
        array[i] = output[i]

# Main function to implement radix sort
def radixSort(array):
    # Get maximum element
    max_element = max(array)

    # Apply Counting Sort to sort elements based on place value.
    place = 1
    while max_element // place > 0:
        countingSort(array, place)
        place *= 10

data = [121, 432, 564, 23, 1, 45, 788]
print('Algoritma Radix Sort 2')
print('Data sebelum diurutkan',data)
radixSort(data)
print('Data sesudah diurutkan',data)