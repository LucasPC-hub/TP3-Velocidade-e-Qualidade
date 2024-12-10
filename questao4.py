"""
 Fibonnati recursivo : Complexidade O(2^n) devido à duplicação de cálculos.
"""
def fib(n):
    print(f"fib({n}) chamada")
    if n <= 1:
        print(f"fib({n}) retorna {n}")
        return n
    resultado = fib(n-1) + fib(n-2)
    print(f"fib({n}) retorna {resultado}")
    return resultado
"""
 Fibonnati fatorial : Complexidade O(n) pois cada número é multiplicado uma vez
"""
def factorial(n):
    print(f"factorial({n}) chamada")
    if n <= 1:
        print(f"factorial({n}) retorna 1")
        return 1
    resultado = n * factorial(n-1)
    print(f"factorial({n}) retorna {resultado}")
    return resultado

# Exemplo de uso
if __name__ == "__main__":
    print("Sequência de Fibonacci:")
    fib(5)
    print("\nCálculo de Fatorial:")
    factorial(5)