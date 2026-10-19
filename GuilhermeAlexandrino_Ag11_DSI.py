"""
Sistema de monitoramento de nível de um reservatório de água.

Simula a leitura de vários níveis e exibe no terminal a situação
de cada um, com a cor correspondente ao grau de risco.

Antes de rodar, instale a biblioteca colorama:
    pip install colorama
"""

from colorama import Fore, Style, init

# Inicializa o colorama (necessário para as cores funcionarem no Windows)
init()

# Lista com as mensagens de alerta: o índice 0 corresponde ao nível 1,
# o índice 1 ao nível 2, e assim por diante até o nível 5.
MENSAGENS = [
    "Nível 1 - Muito baixo (CRÍTICO): risco de falta de água!",
    "Nível 2 - Baixo: atenção, o reservatório está esvaziando.",
    "Nível 3 - Médio: situação normal de operação.",
    "Nível 4 - Alto: reservatório bem abastecido.",
    "Nível 5 - Muito alto (ALERTA): risco de transbordamento!",
]


def definir_cor(nivel):
    """Retorna a cor do terminal de acordo com o nível informado (1 a 5)."""
    if nivel == 1:
        return Fore.RED
    elif nivel == 2:
        return Fore.YELLOW
    elif nivel == 3:
        return Fore.GREEN
    elif nivel == 4:
        return Fore.CYAN
    elif nivel == 5:
        return Fore.BLUE
    else:
        return Fore.WHITE  # nível inválido: cor neutra


def exibir_situacao(nivel):
    """Mostra no terminal a mensagem do nível atual com a cor correspondente."""
    if 1 <= nivel <= 5:
        mensagem = MENSAGENS[nivel - 1]  # nível 1 está no índice 0
    else:
        mensagem = f"Nível {nivel} inválido: leitura fora do esperado."

    cor = definir_cor(nivel)
    print(f"{cor}{mensagem}{Style.RESET_ALL}")


def main():
    print("=== MONITORAMENTO DO RESERVATÓRIO ===\n")

    # Simulação: leituras definidas no próprio código
    leituras = [3, 2, 1, 2, 3, 4, 5, 4]

    for numero, nivel in enumerate(leituras, start=1):
        print(f"Leitura {numero}: ", end="")
        exibir_situacao(nivel)

    # Garante que o terminal volte ao estilo padrão ao final
    print(Style.RESET_ALL, end="")
    print("\nMonitoramento encerrado.")


main()
