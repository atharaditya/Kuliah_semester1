print('bubble sort')
def bubble_sort(array):
    n = len(array) #jumlah list
    for i in range(n): #perulangan pertama
        for j in range(n - i - 1): #perulangan kedua
            #bandingkan masing-masing elemen            
            if array[j] < array[j + 1]:
            #jika lebih besar, tukar.
             array[j], array[j + 1] = array[j + 1], array[j] 
    return array

data = [13,9,4,1,6]
bubble_sort(data)
print(data)

print()

print('selection sort')
def selection_sort(data):  
    n = len(data)
    for i in range(n): # perulangan list elemen
        # cari nilai elemen terendah yang masih tersedia
        min_idx = i
        for j in range(i+1, n):
            if data[min_idx] < data[j]:
                min_idx = j        
        data[i], data[min_idx] = data[min_idx], data[i] # tukar dengan nilai elemen ke-i
    return data

data =[13,9,4,1,6]
selection_sort(data)
print(data)

print()

print('insertion sort')
def insertion_sort(data):
 # perulangan pertama
 for i in range(1, len(data)):
    # ini elemen yang akan kita posisikan
    key_item = data[i]
# kunci index posisi
 j = i - 1
  # lakukan perulangan kedua
 while j >= 0 and data[j] < key_item:
    # menggeser elemen yang lain
    data[j + 1] = data[j]
    j -= 1
    # memposisikan elemen
    data[j + 1] = key_item
 return data

data = [13,9,4,1,6]
insertion_sort(data)
print(data)

print()

print('quick sort')
def quick_sort(arr):
 if len(arr) <= 1:
    return arr
 pivot = arr[len(arr) // 2]
 left = [x for x in arr if x > pivot]
 middle = [x for x in arr if x == pivot]
 right = [x for x in arr if x < pivot]
 return quick_sort(left) + middle + quick_sort(right)

data = [13,9,4,1,6]
print('data :',data)
print('data setelah diurutkan',quick_sort(data))