import os
from colorama import init, Fore, Style

init()


def listar_diretorio(caminho, nivel=0, prefixo=""):
    try:

        if not os.path.exists(caminho):
            print(f"{prefixo}└── {Fore.RED}[Erro: Diretório não encontrado]{Style.RESET_ALL}")
            return


        itens = os.listdir(caminho)


        itens.sort(key=lambda x: (not os.path.isdir(os.path.join(caminho, x)), x))

        for i, item in enumerate(itens):
            caminho_completo = os.path.join(caminho, item)
            is_last = i == len(itens) - 1


            conector = "└──" if is_last else "├──"
            novo_prefixo = prefixo + ("    " if is_last else "│   ")


            if os.path.isdir(caminho_completo):
                print(f"{prefixo}{conector} {Fore.BLUE}{item}/{Style.RESET_ALL}")
                listar_diretorio(caminho_completo, nivel + 1, novo_prefixo)
            else:
                print(f"{prefixo}{conector} {Fore.GREEN}{item}{Style.RESET_ALL}")

    except PermissionError:
        print(f"{prefixo}└── {Fore.RED}[Acesso negado]{Style.RESET_ALL}")
    except Exception as e:
        print(f"{prefixo}└── {Fore.RED}[Erro: {str(e)}]{Style.RESET_ALL}")


def main():
    print("Explorador de Arquivos")
    print("=" * 40)


    diretorio = input("Digite o caminho do diretório (Enter para usar o diretório atual): ").strip()
    if not diretorio:
        diretorio = "."

    print(f"\nExplorando: {os.path.abspath(diretorio)}")
    print("=" * 40)
    listar_diretorio(diretorio)


if __name__ == "__main__":
    main()