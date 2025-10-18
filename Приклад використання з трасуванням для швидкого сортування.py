# Пункт 5: Приклад використання з трасуванням для швидкого сортування

def quicksort_iterative_with_trace(arr):
    """
    Ітеративне швидке сортування з трасуванням
    """
    comparisons = 0
    assignments = 0
    trace_log = []
    
    trace_log.append("=== ПОЧАТОК ІТЕРАТИВНОГО ШВИДКОГО СОРТУВАННЯ ===")
    trace_log.append(f"Початковий масив: {arr}")
    
    if len(arr) <= 1:
        trace_log.append("Масив вже відсортований (розмір ≤ 1)")
        return arr, comparisons, assignments, trace_log
    
    stack = []
    stack.append((0, len(arr) - 1))
    assignments += 1
    trace_log.append(f"Додаємо в стек діапазон [0, {len(arr)-1}]")
    
    step = 1
    
    while stack:
        low, high = stack.pop()
        assignments += 2
        trace_log.append(f"\n--- Крок {step} ---")
        trace_log.append(f"Обробляємо діапазон [{low}, {high}]: {arr[low:high+1]}")
        
        if low < high:
            # Розділення з трасуванням
            pivot_index, comp_part, assign_part, partition_trace = partition_with_trace(arr, low, high)
            comparisons += comp_part
            assignments += assign_part
            trace_log.extend(partition_trace)
            
            trace_log.append(f"Після розділення: {arr[low:high+1]}")
            trace_log.append(f"Індекс розділення: {pivot_index}")
            
            # Додаємо підмасиви в стек
            stack.append((low, pivot_index))
            stack.append((pivot_index + 1, high))
            assignments += 2
            trace_log.append(f"Додаємо в стек: [{low}, {pivot_index}] та [{pivot_index+1}, {high}]")
        else:
            trace_log.append("Діапазон замалий для сортування")
        
        step += 1
        trace_log.append(f"Поточний стан масиву: {arr}")
    
    trace_log.append(f"\n=== ФІНАЛЬНИЙ РЕЗУЛЬТАТ: {arr} ===")
    return arr, comparisons, assignments, trace_log

def partition_with_trace(arr, low, high):
    """
    Функція розділення з трасуванням
    """
    comparisons = 0
    assignments = 0
    trace_log = []
    
    pivot = arr[low]
    assignments += 1
    trace_log.append(f"  Опорний елемент (pivot): {pivot}")
    
    i = low - 1
    j = high + 1
    assignments += 2
    
    trace_log.append(f"  Початкові індекси: i={i}, j={j}")
    
    iteration = 1
    
    while True:
        trace_log.append(f"  --- Ітерація {iteration} ---")
        
        # Рухаємо лівий індекс
        i += 1
        assignments += 1
        trace_log.append(f"    i збільшено до {i}")
        
        while arr[i] < pivot:
            comparisons += 1
            trace_log.append(f"    arr[{i}] = {arr[i]} < {pivot} -> продовжуємо рух i")
            i += 1
            assignments += 1
        comparisons += 1
        trace_log.append(f"    arr[{i}] = {arr[i]} ≥ {pivot} -> зупинка i")
        
        # Рухаємо правий індекс
        j -= 1
        assignments += 1
        trace_log.append(f"    j зменшено до {j}")
        
        while arr[j] > pivot:
            comparisons += 1
            trace_log.append(f"    arr[{j}] = {arr[j]} > {pivot} -> продовжуємо рух j")
            j -= 1
            assignments += 1
        comparisons += 1
        trace_log.append(f"    arr[{j}] = {arr[j]} ≤ {pivot} -> зупинка j")
        
        # Перевірка перетину
        comparisons += 1
        trace_log.append(f"    Перевірка: i={i} >= j={j} -> {i >= j}")
        
        if i >= j:
            trace_log.append(f"    Розділення завершено. Повертаємо j={j}")
            return j, comparisons, assignments, trace_log
        
        # Обмін елементів
        trace_log.append(f"    ОБМІН: arr[{i}]={arr[i]} ↔ arr[{j}]={arr[j]}")
        arr[i], arr[j] = arr[j], arr[i]
        assignments += 3
        trace_log.append(f"    Після обміну: {arr[low:high+1]}")
        
        iteration += 1

def quicksort_recursive_with_trace(arr, low=0, high=None, depth=0):
    """
    Рекурсивне швидке сортування з трасуванням
    """
    indent = "  " * depth
    trace_log = []
    
    if high is None:
        high = len(arr) - 1
    
    trace_log.append(f"{indent}▶ quicksort(arr, {low}, {high}) - {arr[low:high+1]}")
    
    comparisons = 0
    assignments = 0
    recursive_calls = 1
    
    if low < high:
        # Розділення з трасуванням
        pivot_index, comp_part, assign_part, partition_trace = partition_with_trace(arr, low, high)
        comparisons += comp_part
        assignments += assign_part
        
        # Додаємо трасування розділення з відступами
        for line in partition_trace:
            trace_log.append(f"{indent}  {line}")
        
        trace_log.append(f"{indent}  Індекс розділення: {pivot_index}")
        trace_log.append(f"{indent}  Після розділення: {arr[low:high+1]}")
        
        # Рекурсивні виклики
        trace_log.append(f"{indent}  Рекурсивний виклик для лівого підмасиву [{low}, {pivot_index}]")
        comp_left, assign_left, rec_left, trace_left = quicksort_recursive_with_trace(arr, low, pivot_index, depth + 1)
        
        trace_log.append(f"{indent}  Рекурсивний виклик для правого підмасиву [{pivot_index+1}, {high}]")
        comp_right, assign_right, rec_right, trace_right = quicksort_recursive_with_trace(arr, pivot_index + 1, high, depth + 1)
        
        comparisons += comp_left + comp_right
        assignments += assign_left + assign_right
        recursive_calls += rec_left + rec_right
        
        trace_log.extend(trace_left)
        trace_log.extend(trace_right)
        
        trace_log.append(f"{indent}  ✅ Підмасив [{low}, {high}] відсортовано: {arr[low:high+1]}")
    else:
        trace_log.append(f"{indent}  Базовий випадок - підмасив вже відсортований")
    
    trace_log.append(f"{indent}◀ Повертаємося з quicksort(arr, {low}, {high})")
    
    return comparisons, assignments, recursive_calls, trace_log

# ТЕСТУВАННЯ З ТРАСУВАННЯМ
print("=== ПУНКТ 5: ПРИКЛАД ВИКОРИСТАННЯ З ТРАСУВАННЯМ ===")
print("Варіант №9: [12, 23, 67, 65, 50, 70, 80, 61, 92]")
print()

my_sequence = [12, 23, 67, 65, 50, 70, 80, 61, 92]

print("5.1 ІТЕРАТИВНИЙ АЛГОРИТМ З ТРАСУВАННЯМ:")
print("=" * 60)

arr_iter = my_sequence.copy()
print(f"Початковий масив: {arr_iter}")
print("\nТРАСУВАННЯ:")
print("-" * 50)

sorted_iter, comp_iter, assign_iter, trace_iter = quicksort_iterative_with_trace(arr_iter)

for line in trace_iter:
    print(line)

print(f"\nПІДСУМОК ІТЕРАТИВНОГО АЛГОРИТМУ:")
print(f"Відсортований масив: {sorted_iter}")
print(f"Порівнянь: {comp_iter}, Присвоювань: {assign_iter}")
print(f"Правильність: {sorted_iter == sorted(my_sequence)}")

print("\n" + "=" * 60)
print("5.2 РЕКУРСИВНИЙ АЛГОРИТМ З ТРАСУВАННЯМ:")
print("=" * 60)

arr_rec = my_sequence.copy()
print(f"Початковий масив: {arr_rec}")
print("\nТРАСУВАННЯ:")
print("-" * 50)

comp_rec, assign_rec, rec_calls, trace_rec = quicksort_recursive_with_trace(arr_rec)

for line in trace_rec:
    print(line)

print(f"\nПІДСУМОК РЕКУРСИВНОГО АЛГОРИТМУ:")
print(f"Відсортований масив: {arr_rec}")
print(f"Порівнянь: {comp_rec}, Присвоювань: {assign_rec}, Рекурсивних викликів: {rec_calls}")
print(f"Правильність: {arr_rec == sorted(my_sequence)}")

print("\n" + "=" * 60)
print("5.3 ПОРІВНЯЛЬНА ТАБЛИЦЯ:")
print("=" * 60)

print(f"{'Алгоритм':<25} {'Порівнянь':<12} {'Присвоювань':<12} {'Рекурсивних викликів':<20}")
print("-" * 70)
print(f"{'Ітеративний':<25} {comp_iter:<12} {assign_iter:<12} {'-':<20}")
print(f"{'Рекурсивний':<25} {comp_rec:<12} {assign_rec:<12} {rec_calls:<20}")