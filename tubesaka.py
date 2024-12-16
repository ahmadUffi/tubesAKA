import time
import pandas as pd
import matplotlib.pyplot as plt
from tabulate import tabulate

# Fungsi Bubble Sort (Iteratif)
def bubble_sort_iterative(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break

# Fungsi Bubble Sort (Rekursif)
def bubble_sort_recursive(arr):
    n = len(arr)
    if n == 1:
        return arr
    for i in range(n-1):
        if arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
    return bubble_sort_recursive(arr[:-1]) + [arr[-1]]

# Fungsi Quick Sort (Rekursif)
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# Fungsi Quick Sort (Iteratif)
def quick_sort_iterative(arr):
    if len(arr) <= 1:
        return arr
    
    stack = [(0, len(arr) - 1)]
    while stack:
        start, end = stack.pop()
        pivot = arr[(start + end) // 2]
        left = start
        right = end
        
        while left <= right:
            while arr[left] < pivot:
                left += 1
            while arr[right] > pivot:
                right -= 1
            if left <= right:
                arr[left], arr[right] = arr[right], arr[left]
                left += 1
                right -= 1
        
        if start < right:
            stack.append((start, right))
        if left < end:
            stack.append((left, end))
    
    return arr

# Menghitung waktu eksekusi
def measure_time(sort_function, data):
    start_time = time.time()
    sort_function(data)
    return time.time() - start_time

# Data untuk pengujian
people = ['Ahmad', 'uffi', 'Lestari', 'makruf', 'rifqi', 'taufiqurrahma', 'salman', 'gilang', 'satria', 'mahrus', 'software', 'engginering']

# Menyimpan hasil
results = []

for person in people:
    # Generate data acak berdasarkan panjang nama
    data = [ord(char) for char in person]  # Menggunakan nilai ASCII dari karakter nama
    
    # Ukur waktu untuk Bubble Sort (Iteratif)
    bubble_iter_time = measure_time(bubble_sort_iterative, data.copy())
    
    # Ukur waktu untuk Bubble Sort (Rekursif)
    bubble_recur_time = measure_time(bubble_sort_recursive, data.copy())
    
    # Ukur waktu untuk Quick Sort (Rekursif)
    quick_recur_time = measure_time(quick_sort, data.copy())
    
    # Ukur waktu untuk Quick Sort (Iteratif)
    quick_iter_time = measure_time(quick_sort_iterative, data.copy())
    
    results.append({
        'Person': person,
        'Bubble Sort Iterative Time (s)': bubble_iter_time,
        'Bubble Sort Recursive Time (s)': bubble_recur_time,
        'Quick Sort Iterative Time (s)': quick_iter_time,
        'Quick Sort Recursive Time (s)': quick_recur_time
    })

# Membuat DataFrame
df = pd.DataFrame(results)

# Menampilkan tabel dengan tabulate
print(tabulate(df, headers='keys', tablefmt='grid'))

# Membuat grafik
plt.figure(figsize=(12, 6))
plt.plot(df['Person'], df['Bubble Sort Iterative Time (s)'], marker='o', label='Bubble Sort (Iteratif)', color='orange')
plt.plot(df['Person'], df['Bubble Sort Recursive Time (s)'], marker='o', label='Bubble Sort (Rekursif)', color='red')
plt.plot(df['Person'], df['Quick Sort Iterative Time (s)'], marker='o', label='Quick Sort (Iteratif)', color='blue')
plt.plot(df['Person'], df['Quick Sort Recursive Time (s)'], marker='o', label='Quick Sort (Rekursif)', color='green')
plt.title('Performance Comparison: Bubble Sort vs Quick Sort')
plt.xlabel('Input (Person)')
plt.ylabel('Execution Time (seconds)')
plt.legend()
plt.grid()
plt.show()
