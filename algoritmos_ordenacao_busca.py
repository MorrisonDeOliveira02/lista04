import random
import time

# --- Questões 1 a 3 e 9: Algoritmos de Ordenação Instrumentados ---

def insertion_sort_instrumented(arr):
    """Implementa Insertion Sort contabilizando deslocamentos e comparações."""
    arr = arr.copy()
    comparisons = 0
    deslocamentos_por_iteracao = []
    
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        shifts = 0
        
        while j >= 0:
            comparisons += 1
            if arr[j] > key:
                arr[j + 1] = arr[j]
                shifts += 1
                j -= 1
            else:
                break
                
        arr[j + 1] = key
        deslocamentos_por_iteracao.append(shifts)
        
    return arr, comparisons, deslocamentos_por_iteracao

def merge_sort_instrumented(arr):
    """Implementa Merge Sort contabilizando comparações."""
    if len(arr) <= 1:
        return arr, 0
        
    mid = len(arr) // 2
    left, comp_left = merge_sort_instrumented(arr[:mid])
    right, comp_right = merge_sort_instrumented(arr[mid:])
    
    merged, comp_merge = merge_instrumented(left, right)
    
    return merged, comp_left + comp_right + comp_merge

def merge_instrumented(left, right):
    """Intercala duas listas contabilizando comparações."""
    merged = []
    comparisons = 0
    i = j = 0
    
    while i < len(left) and j < len(right):
        comparisons += 1
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
            
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged, comparisons


# --- Questão 4 e 5: Algoritmos de Busca Instrumentados ---

def binary_search_instrumented(arr, target):
    """Implementa Busca Binária e regista as posições visitadas e comparações."""
    left, right = 0, len(arr) - 1
    visited_indices = []
    comparisons = 0
    
    while left <= right:
        mid = (left + right) // 2
        visited_indices.append(mid)
        comparisons += 1
        
        if arr[mid] == target:
            return mid, visited_indices, comparisons
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
            
    return -1, visited_indices, comparisons


# --- Geração de Resultados e Tabela (Execução) ---

if __name__ == "__main__":
    print("=== QUESTÃO 1 ===")
    v1 = [7, 3, 9, 2, 8, 1]
    _, _, shifts = insertion_sort_instrumented(v1)
    for idx, s in enumerate(shifts, 1):
        print(f"Iteração {idx} (laço externo): {s} deslocamentos.")

    print("\n=== QUESTÃO 3 ===")
    lista_a = [2, 5, 8, 11]
    lista_b = [1, 3, 9, 12]
    resultado_merge, comps_merge = merge_instrumented(lista_a, lista_b)
    print(f"Lista intercalada: {resultado_merge}")
    print(f"Total de comparações: {comps_merge}")
    
    print("\n=== QUESTÃO 4 ===")
    v4 = [1, 3, 5, 7, 9, 11, 13, 15]
    for target in [13, 4]:
        _, visited, comps = binary_search_instrumented(v4, target)
        print(f"Busca pelo {target} -> Posições visitadas: {visited} | Comparações: {comps}")

    print("\n=== QUESTÃO 5 ===")
    v5 = [7, 2, 9, 1, 5, 8, 3, 6]
    resultado, visited_v5, _ = binary_search_instrumented(v5, 9)
    print(f"Busca pelo 9 (Vetor Desordenado) -> Índices do caminho: {visited_v5} | Devolveu: {resultado}")

    print("\n=== QUESTÃO 9 (Tabela de Comparações) ===")
    tamanhos = [100, 1000, 10000, 100000]
    print(f"{'n':>8} | {'Insertion Sort':>20} | {'Merge Sort':>20}")
    print("-" * 55)
    
    for n in tamanhos:
        arr_aleatorio = [random.randint(1, 100000) for _ in range(n)]
        
        # Para n muito grande, o Insertion Sort é extremamente lento, 
        # opta-se por limitá-lo nesta demonstração ou aguardar pacientemente.
        if n <= 10000: 
            _, comp_insert = insertion_sort_instrumented(arr_aleatorio)
        else:
            comp_insert = "O(n^2) - Ignorado p/ poupar tempo" 
            
        _, comp_merge = merge_sort_instrumented(arr_aleatorio)
        print(f"{n:>8} | {str(comp_insert):>20} | {comp_merge:>20}")
