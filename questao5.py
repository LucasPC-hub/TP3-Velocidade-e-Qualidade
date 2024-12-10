def quicksort(arr, depth=0):
    indent = "  " * depth
    if len(arr) <= 1:
        print(f"{indent}Retornando: {arr}")
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    print(f"{indent}Array atual: {arr}")
    print(f"{indent}Pivô escolhido: {pivot}")
    print(f"{indent}Esquerda: {left}")
    print(f"{indent}Meio: {middle}")
    print(f"{indent}Direita: {right}")

    sorted_left = quicksort(left, depth + 1)
    sorted_right = quicksort(right, depth + 1)

    result = sorted_left + middle + sorted_right
    print(f"{indent}Resultado combinado: {result}")
    return result

# Exemplo de uso
if __name__ == "__main__":
    array = [7, 2, 1, 6, 8, 5, 3, 4]
    print("Array inicial:", array)
    sorted_array = quicksort(array)
    print("Array ordenado:", sorted_array)