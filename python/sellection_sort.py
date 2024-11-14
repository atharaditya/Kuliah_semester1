def selection_sort(data):  
    n = len(data)
    for i in range(n): # perulangan list elemen
        # cari nilai elemen terendah yang masih tersedia
        min_idx = i
        for j in range(i+1, n):
            if data[min_idx] > data[j]:
                min_idx = j        
        data[i], data[min_idx] = data[min_idx], data[i] # tukar dengan nilai elemen ke-i
    return data

data=[19,8,2,24]
selection_sort(data)
print(data)