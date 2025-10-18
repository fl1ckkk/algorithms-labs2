# Пункт 4: Реалізація алгоритмів швидкого сортування

def quicksort_iterative(arr):
    """
    Ітеративна реалізація швидкого сортування за схемою Хоара
    """
    comparisons = 0
    assignments = 0
    
    if len(arr) <= 1:
        return arr, comparisons, assignments
    
    # Використовуємо стек для імітації рекурсії
    stack = []
    stack.append((0, len(arr) - 1))
    assignments += 1
    
    while stack:
        low, high = stack.pop()
        assignments += 2
        
        if low < high:
            # Розділення масиву
            pivot_index, comp_part, assign_part = partition(arr, low, high)
            comparisons += comp_part
            assignments += assign_part
            
            # Додаємо підмасиви в стек
            stack.append((low, pivot_index))
            stack.append((pivot_index + 1, high))
            assignments += 2
    
    return arr, comparisons, assignments

def quicksort_recursive(arr, low=0, high=None):
    """
    Рекурсивна реалізація швидкого сортування за схемою Хоара
    """
    comparisons = 0
    assignments = 0
    recursive_calls = 1
    
    if high is None:
        high = len(arr) - 1
        assignments += 1
    
    if low < high:
        # Розділення масиву
        pivot_index, comp_part, assign_part = partition(arr, low, high)
        comparisons += comp_part
        assignments += assign_part
        
        # Рекурсивні виклики для підмасивів
        comp_left, assign_left, rec_left = quicksort_recursive(arr, low, pivot_index)
        comp_right, assign_right, rec_right = quicksort_recursive(arr, pivot_index + 1, high)
        
        comparisons += comp_left + comp_right
        assignments += assign_left + assign_right
        recursive_calls += rec_left + rec_right
    
    return comparisons, assignments, recursive_calls

def partition(arr, low, high):
    """
    Функція розділення за схемою Хоара
    """
    comparisons = 0
    assignments = 0
    
    # Вибір опорного елемента (перший елемент)
    pivot = arr[low]
    assignments += 1
    
    # Ініціалізація індексів
    i = low - 1
    j = high + 1
    assignments += 2
    
    while True:
        # Рухаємо лівий індекс вправо
        i += 1
        assignments += 1
        while arr[i] < pivot:
            comparisons += 1
            i += 1
            assignments += 1
        comparisons += 1  # останнє порівняння, що вийшло з циклу
        
        # Рухаємо правий індекс вліво
        j -= 1
        assignments += 1
        while arr[j] > pivot:
            comparisons += 1
            j -= 1
            assignments += 1
        comparisons += 1  # останнє порівняння, що вийшло з циклу
        
        # Перевірка на перетин індексів
        comparisons += 1
        if i >= j:
            return j, comparisons, assignments
        
        # Обмін елементів
        arr[i], arr[j] = arr[j], arr[i]
        assignments += 3

# ТЕСТУВАННЯ АЛГОРИТМІВ ШВИДКОГО СОРТУВАННЯ
print("=== ПУНКТ 4: РЕАЛІЗАЦІЯ АЛГОРИТМІВ ШВИДКОГО СОРТУВАННЯ ===")
print("Варіант №9: [12, 23, 67, 65, 50, 70, 80, 61, 92]")
print()

my_sequence = [12, 23, 67, 65, 50, 70, 80, 61, 92]

print("4.1 ІТЕРАТИВНИЙ АЛГОРИТМ ШВИДКОГО СОРТУВАННЯ:")
print("-" * 50)

arr_iter = my_sequence.copy()
print(f"До сортування: {arr_iter}")

sorted_iter, comp_iter, assign_iter = quicksort_iterative(arr_iter)
print(f"Після сортування: {sorted_iter}")
print(f"Кількість порівнянь: {comp_iter}")
print(f"Кількість присвоювань: {assign_iter}")
print(f"Перевірка правильності: {sorted_iter == sorted(my_sequence)}")
print()

print("4.2 РЕКУРСИВНИЙ АЛГОРИТМ ШВИДКОГО СОРТУВАННЯ:")
print("-" * 50)

arr_rec = my_sequence.copy()
print(f"До сортування: {arr_rec}")

comp_rec, assign_rec, rec_calls = quicksort_recursive(arr_rec)
print(f"Після сортування: {arr_rec}")
print(f"Кількість порівнянь: {comp_rec}")
print(f"Кількість присвоювань: {assign_rec}")
print(f"Кількість рекурсивних викликів: {rec_calls}")
print(f"Перевірка правильності: {arr_rec == sorted(my_sequence)}")
print()

print("4.3 ПОРІВНЯННЯ АЛГОРИТМІВ ШВИДКОГО СОРТУВАННЯ:")
print("-" * 50)

print(f"{'Алгоритм':<30} {'Порівнянь':<12} {'Присвоювань':<12} {'Рекурсивних викликів':<20}")
print("-" * 75)
print(f"{'Ітеративний':<30} {comp_iter:<12} {assign_iter:<12} {'-':<20}")
print(f"{'Рекурсивний':<30} {comp_rec:<12} {assign_rec:<12} {rec_calls:<20}")

print(f"\n4.4 ОСОБЛИВОСТІ РЕАЛІЗАЦІЇ:")
print(f"• Використана схема Хоара")
print(f"• Опорний елемент: перший елемент підмасиву")
print(f"• Алгоритм нестабільний")
print(f"• Середня складність: O(n log n)")
print(f"• Найгірша складність: O(n²)")