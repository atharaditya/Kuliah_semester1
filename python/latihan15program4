import time
awal = time.time()

def shellSort(arr):
    n = len(arr)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap][1] > temp[1]:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2

    return arr

arr = [("Atha", 13, 8.3), ("Afril", 30, 1.5), ("Asep", 7, 3.8), ("Iqbal", 45, 8.6), ("Fellix", 55, 7.9)]
print("Array sebelum diurutkan:")
print(arr)

arr = shellSort(arr)

print("Array setelah diurutkan:")
print(arr)
print()
akhir = time.time()
cepat = (akhir-awal)
print('kecepatan sortingnya adalah : ',cepat)