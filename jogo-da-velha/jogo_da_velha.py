# Função para imprimir o tabuleiro
def imprimir_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print("|".join(linha))
        print("-" * 5)

# Função para verificar se há um vencedor
def verificar_vencedor(tabuleiro, jogador):
    # Verificar linhas
    for linha in tabuleiro:
        if all(s == jogador for s in linha):
            return True
    
    # Verificar Colunas
    for col in range(3):
        if all (tabuleiro[row][col] == jogador for row in range(3)):
            return True
    
    # Verificar diagonais
    if all(tabuleiro[i][i] == jogador for i in range(3)) or all(tabuleiro[i][2 - 1] == jogador for i in range(3)):
        return True

    return False

# Fução para verificar se o tabuleiro está cheio
def tabuleiro_cheio(tabuleiro):
    for linha in tabuleiro:
        if any(s == " " for s in linha):
            return False
    
    return True

# Função principal do jogo
def jogo_da_velha():
    tabuleiro = [[" " for _ in range(3)] for _ in range(3)]
    jogador_atual = "x"

    while True:
        imprimir_tabuleiro(tabuleiro)
        print(f"Jogador {jogador_atual}, é sua vez.")

        while True:
            try:
                linha = int(input("Digite a linha (1-3): ")) - 1
                coluna = int(input("Digite a coluna (1-3): ")) - 1
                if tabuleiro[linha][coluna] == " ":
                    tabuleiro[linha][coluna] = jogador_atual
                    break
                else:
                    print("Posição já ocupada, escolha outra.")
            except (ValueError, IndexError):
                print("Entrada inválida. Por favor, digite números entre 1 e 3.")

        if verificar_vencedor(tabuleiro, jogador_atual):
            imprimir_tabuleiro(tabuleiro)
            print(f"Jogador {jogador_atual} venceu!")
            break
        
        if tabuleiro_cheio(tabuleiro):
            imprimir_tabuleiro(tabuleiro)
            print("Empate!")
            break

        jogador_atual = "O" if jogador_atual == "x" else "x"

if __name__ == "__main__":
    jogo_da_velha()