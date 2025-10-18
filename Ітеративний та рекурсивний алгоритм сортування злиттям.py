# Пункт 1: Реалізація алгоритмів сортування злиттям

def merge_sort_iterative(arr):
    """
    Ітеративна реалізація сортування злиттям
    """
    n = len(arr)
    comparisons = 0
    assignments = 0
    size = 1
    
    while size < n:
        left = 0
        while left < n:
            mid = min(left + size, n)
            right = min(left + 2 * size, n)
            
            comp, assign = merge(arr, left, mid, right)
            comparisons += comp
            assignments += assign
            
            left += 2 * size
        size *= 2
    
    return arr, comparisons, assignments

def merge(arr, left, mid, right):
    """
    Допоміжна функція для злиття двох відсортованих підмасивів
    """
    comparisons = 0
    assignments = 0
    
    left_arr = arr[left:mid]
    right_arr = arr[mid:right]
    assignments += (mid - left) + (right - mid)
    
    i = j = 0
    k = left
    assignments += 3
    
    while i < len(left_arr) and j < len(right_arr):
        comparisons += 1
        if left_arr[i] <= right_arr[j]:
            arr[k] = left_arr[i]
            i += 1
            assignments += 1
        else:
            arr[k] = right_arr[j]
            j += 1
            assignments += 1
        k += 1
        assignments += 1
    
    while i < len(left_arr):
        arr[k] = left_arr[i]
        i += 1
        k += 1
        assignments += 1
    
    while j < len(right_arr):
        arr[k] = right_arr[j]
        j += 1
        k += 1
        assignments += 1
    
    return comparisons, assignments

def merge_sort_recursive(arr):
    """
    Рекурсивна реалізація сортування злиттям
    """
    if len(arr) <= 1:
        return arr, 0, 0, 0
    
    comparisons = 0
    assignments = 0
    recursive_calls = 2
    
    mid = len(arr) // 2
    assignments += 1
    
    left_arr, comp_left, assign_left, rec_left = merge_sort_recursive(arr[:mid])
    right_arr, comp_right, assign_right, rec_right = merge_sort_recursive(arr[mid:])
    
    comparisons += comp_left + comp_right
    assignments += assign_left + assign_right
    recursive_calls += rec_left + rec_right
    
    merged_arr, comp_merge, assign_merge = merge_recursive(left_arr, right_arr)
    comparisons += comp_merge
    assignments += assign_merge
    
    return merged_arr, comparisons, assignments, recursive_calls

def merge_recursive(left, right):
    """
    Допоміжна функція для злиття двох відсортованих масивів
    """
    result = []
    comparisons = 0
    assignments = 0
    i = j = 0
    assignments += 2
    
    while i < len(left) and j < len(right):
        comparisons += 1
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
        assignments += 1
    
    while i < len(left):
        result.append(left[i])
        i += 1
        assignments += 1
    
    while j < len(right):
        result.append(right[j])
        j += 1
        assignments += 1
    
    return result, comparisons, assignments

# ТЕСТУВАННЯ АЛГОРИТМІВ
print("=== ПУНКТ 1: РЕАЛІЗАЦІЯ АЛГОРИТМІВ СОРТУВАННЯ ЗЛИТТЯМ ===")
print("Варіант №9: [12, 23, 67, 65, 50, 70, 80, 61, 92]")
print()

my_sequence = [12, 23, 67, 65, 50, 70, 80, 61, 92]

print("1.1 ІТЕРАТИВНИЙ АЛГОРИТМ:")
arr_iter = my_sequence.copy()
sorted_iter, comp_iter, assign_iter = merge_sort_iterative(arr_iter)
print(f"Вхідний масив: {my_sequence}")
print(f"Відсортований масив: {sorted_iter}")
print(f"Кількість порівнянь: {comp_iter}")
print(f"Кількість присвоювань: {assign_iter}")
print()

print("1.2 РЕКУРСИВНИЙ АЛГОРИТМ:")
arr_rec = my_sequence.copy()
sorted_rec, comp_rec, assign_rec, rec_calls = merge_sort_recursive(arr_rec)
print(f"Вхідний масив: {my_sequence}")
print(f"Відсортований масив: {sorted_rec}")
print(f"Кількість порівнянь: {comp_rec}")
print(f"Кількість присвоювань: {assign_rec}")
print(f"Кількість рекурсивних викликів: {rec_calls}")
print()

print("1.3 ПЕРЕВІРКА КОРЕКТНОСТІ:")
print(f"Обидва алгоритми дали однаковий результат: {sorted_iter == sorted_rec}")
print(f"Масив відсортований правильно: {sorted_iter == sorted(my_sequence)}")