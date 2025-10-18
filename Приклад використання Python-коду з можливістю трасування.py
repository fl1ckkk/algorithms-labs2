# Пункт 2: Приклад використання з трасуванням

def merge_sort_iterative_with_trace(arr):
    """
    Ітеративне сортування злиттям з трасуванням
    """
    n = len(arr)
    comparisons = 0
    assignments = 0
    size = 1
    trace_log = []
    
    trace_log.append(f"ПОЧАТОК ІТЕРАТИВНОГО АЛГОРИТМУ")
    trace_log.append(f"Початковий масив: {arr}")
    
    while size < n:
        trace_log.append(f"--- Розмір підмасивів: {size} ---")
        left = 0
        while left < n:
            mid = min(left + size, n)
            right = min(left + 2 * size, n)
            
            trace_log.append(f"Злиття: arr[{left}:{mid}] = {arr[left:mid]} та arr[{mid}:{right}] = {arr[mid:right]}")
            
            comp, assign, merge_trace = merge_with_trace(arr, left, mid, right)
            comparisons += comp
            assignments += assign
            trace_log.extend(merge_trace)
            
            trace_log.append(f"Проміжний результат: {arr}")
            left += 2 * size
        size *= 2
    
    trace_log.append(f"ФІНАЛЬНИЙ РЕЗУЛЬТАТ: {arr}")
    return arr, comparisons, assignments, trace_log

def merge_with_trace(arr, left, mid, right):
    """
    Злиття з трасуванням
    """
    comparisons = 0
    assignments = 0
    trace_log = []
    
    left_arr = arr[left:mid]
    right_arr = arr[mid:right]
    assignments += (mid - left) + (right - mid)
    
    trace_log.append(f"  Лівий підмасив: {left_arr}")
    trace_log.append(f"  Правий підмасив: {right_arr}")
    
    i = j = 0
    k = left
    assignments += 3
    
    trace_log.append("  Початок злиття:")
    
    while i < len(left_arr) and j < len(right_arr):
        comparisons += 1
        trace_log.append(f"    Порівнюємо {left_arr[i]} та {right_arr[j]}")
        if left_arr[i] <= right_arr[j]:
            arr[k] = left_arr[i]
            trace_log.append(f"    Додаємо {left_arr[i]} з лівого масиву")
            i += 1
            assignments += 1
        else:
            arr[k] = right_arr[j]
            trace_log.append(f"    Додаємо {right_arr[j]} з правого масиву")
            j += 1
            assignments += 1
        k += 1
        assignments += 1
    
    while i < len(left_arr):
        arr[k] = left_arr[i]
        trace_log.append(f"    Додаємо залишок з лівого: {left_arr[i]}")
        i += 1
        k += 1
        assignments += 1
    
    while j < len(right_arr):
        arr[k] = right_arr[j]
        trace_log.append(f"    Додаємо залишок з правого: {right_arr[j]}")
        j += 1
        k += 1
        assignments += 1
    
    trace_log.append(f"  Злиття завершено")
    return comparisons, assignments, trace_log

def merge_sort_recursive_with_trace(arr, depth=0):
    """
    Рекурсивне сортування злиттям з трасуванням
    """
    indent = "  " * depth
    trace_log = []
    
    trace_log.append(f"{indent}ВХІД: {arr} (глибина: {depth})")
    
    if len(arr) <= 1:
        trace_log.append(f"{indent}Базовий випадок -> {arr}")
        return arr, 0, 0, 1, trace_log
    
    comparisons = 0
    assignments = 0
    recursive_calls = 2
    
    mid = len(arr) // 2
    assignments += 1
    
    trace_log.append(f"{indent}Розділяємо на: {arr[:mid]} та {arr[mid:]}")
    
    # Рекурсивні виклики
    left_arr, comp_left, assign_left, rec_left, trace_left = merge_sort_recursive_with_trace(arr[:mid], depth + 1)
    right_arr, comp_right, assign_right, rec_right, trace_right = merge_sort_recursive_with_trace(arr[mid:], depth + 1)
    
    comparisons += comp_left + comp_right
    assignments += assign_left + assign_right
    recursive_calls += rec_left + rec_right
    trace_log.extend(trace_left)
    trace_log.extend(trace_right)
    
    trace_log.append(f"{indent}Зливаємо: {left_arr} та {right_arr}")
    
    # Злиття
    merged_arr, comp_merge, assign_merge, merge_trace = merge_recursive_with_trace(left_arr, right_arr, depth)
    comparisons += comp_merge
    assignments += assign_merge
    trace_log.extend(merge_trace)
    
    trace_log.append(f"{indent}РЕЗУЛЬТАТ ЗЛИТТЯ: {merged_arr}")
    
    return merged_arr, comparisons, assignments, recursive_calls, trace_log

def merge_recursive_with_trace(left, right, depth=0):
    """
    Злиття для рекурсивного алгоритму з трасуванням
    """
    indent = "  " * depth
    result = []
    comparisons = 0
    assignments = 0
    trace_log = []
    i = j = 0
    assignments += 2
    
    trace_log.append(f"{indent}Початок злиття: left={left}, right={right}")
    
    while i < len(left) and j < len(right):
        comparisons += 1
        trace_log.append(f"{indent}Порівняння: {left[i]} <= {right[j]} -> {left[i] <= right[j]}")
        if left[i] <= right[j]:
            result.append(left[i])
            trace_log.append(f"{indent}Додаємо {left[i]} з лівого")
            i += 1
        else:
            result.append(right[j])
            trace_log.append(f"{indent}Додаємо {right[j]} з правого")
            j += 1
        assignments += 1
    
    while i < len(left):
        result.append(left[i])
        trace_log.append(f"{indent}Додаємо залишок з лівого: {left[i]}")
        i += 1
        assignments += 1
    
    while j < len(right):
        result.append(right[j])
        trace_log.append(f"{indent}Додаємо залишок з правого: {right[j]}")
        j += 1
        assignments += 1
    
    trace_log.append(f"{indent}Злиття завершено: {result}")
    return result, comparisons, assignments, trace_log

# ТЕСТУВАННЯ З ТРАСУВАННЯМ
print("\n" + "="*70)
print("ПУНКТ 2: ПРИКЛАД ВИКОРИСТАННЯ З ТРАСУВАННЯМ")
print("="*70)

my_sequence = [12, 23, 67, 65, 50, 70, 80, 61, 92]

print("2.1 ІТЕРАТИВНИЙ АЛГОРИТМ З ТРАСУВАННЯМ:")
print("-" * 50)

arr_iter = my_sequence.copy()
sorted_iter, comp_iter, assign_iter, trace_iter = merge_sort_iterative_with_trace(arr_iter)

# Виводимо трасування
for line in trace_iter:
    print(line)

print(f"\nПідсумок ітеративного алгоритму:")
print(f"Відсортований масив: {sorted_iter}")
print(f"Порівнянь: {comp_iter}, Присвоювань: {assign_iter}")

print("\n2.2 РЕКУРСИВНИЙ АЛГОРИТМ З ТРАСУВАННЯМ:")
print("-" * 50)

arr_rec = my_sequence.copy()
sorted_rec, comp_rec, assign_rec, rec_calls, trace_rec = merge_sort_recursive_with_trace(arr_rec)

# Виводимо трасування
for line in trace_rec:
    print(line)

print(f"\nПідсумок рекурсивного алгоритму:")
print(f"Відсортований масив: {sorted_rec}")
print(f"Порівнянь: {comp_rec}, Присвоювань: {assign_rec}, Рекурсивних викликів: {rec_calls}")