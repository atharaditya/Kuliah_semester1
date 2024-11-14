import time
awal = time.time()

def shellSort(arr):
    n = len(arr)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2

    return arr

arr = [3.2, 4.5, 1.8, 2.6, 9.1, 15.3]
print("Array sebelum diurutkan:")
print(arr)

arr = shellSort(arr)

print("Array setelah diurutkan:")
print(arr)
print()
akhir = time.time()
cepat = (akhir-awal)
print('kecepatan sortingnya adalah : ',cepat)