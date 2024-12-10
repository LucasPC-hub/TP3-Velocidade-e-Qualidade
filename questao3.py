def visualizar_torres(torres, n):
    """Visualiza o estado atual das torres."""
    print("\n" + "=" * 50)

    # Encontra a altura máxima das torres
    max_altura = n

    # Imprime as torres de cima para baixo
    for nivel in range(max_altura - 1, -1, -1):
        for torre in torres:
            if nivel < len(torre):
                disco = torre[nivel]
                # Cria uma representação visual do disco
                print(f"[{'#' * disco:^{n * 2}}]", end=" ")
            else:
                # Torre vazia neste nível
                print(f"[{' ':{n * 2}}]", end=" ")
        print()  # Nova linha após cada nível

    # Imprime as bases das torres
    for i in range(3):
        print(f" {'=' * (n * 2)} ", end=" ")
    print()

    # Imprime os rótulos das torres
    print("   A   ", end=" ")
    print("   B   ", end=" ")
    print("   C   ")
    print("=" * 50)


def hanoi_visual(n):
    """Resolve Torre de Hanói com visualização."""
    # Inicializa as torres
    torres = {
        'A': list(range(n, 0, -1)),  # Torre inicial com discos ordenados
        'B': [],  # Torre auxiliar vazia
        'C': []  # Torre destino vazia
    }

    def mover_disco(origem, destino):
        disco = torres[origem].pop()
        torres[destino].append(disco)
        print(f"\nMovendo disco {disco} de {origem} para {destino}")
        visualizar_torres([torres['A'], torres['B'], torres['C']], n)

    def hanoi_recursivo(n, origem, destino, auxiliar):
        if n == 1:
            mover_disco(origem, destino)
            return

        hanoi_recursivo(n - 1, origem, auxiliar, destino)
        mover_disco(origem, destino)
        hanoi_recursivo(n - 1, auxiliar, destino, origem)

    print("\nEstado Inicial:")
    visualizar_torres([torres['A'], torres['B'], torres['C']], n)
    hanoi_recursivo(n, 'A', 'C', 'B')



print("🗼 Torre de Hanói")
print("=" * 40)
hanoi_visual(3)