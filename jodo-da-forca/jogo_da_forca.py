import random

palavras = ["python", "programacao", "desenvolvimento", "algoritmo", "computador"]

def escolher_palavra(palavras):
    return random.choice(palavras)

def exibir_palavra(palavra, letras_adivinhadas):
    exibir = ""
    for letura in palavra:
        if letra in letras_adivinhadas:
            exibir += letra
        else:
            exibir += "_"
    return exibir

def jogo_da_forca():
    palavra = escolher_palavra(palavras)
    letras_adivinhadas = set()
    tentativas = 6

    print("Bem-vindo ao Jogo da Forca!")
    print("A palavra tem", len(palavra), "letras.")

    while tentativas > 0:
        print("\n" + exibir_palavra(palavra, letras_adivinhadas))
        print(f"Você tem {tentativas} tentativas restantes.")

        tentativa = input("Adivinhe uma letra: ").lower()
        if tentativa in letras_adivinhadas:
            print("Você já adivinhou essa letra.")
        elif tentativa in palavra:
            print("Boa! A letra está na palavra.")
            letras_adivinhadas.add(tentativa)
        else:
            print("Que pena! A letra não está na palavra.")
            tentativas -= 1
            letras_adivinhadas.add(tentativa)

        if all(letra in letras_adivinhadas for letra in palavra):
            print("\nParabéns! Você adivinhou a palavra:", palavra)
            break
    else:
        print("\nVocê perdeu! A palavra era:", palavra)

if __name__ == "__main__":
    jogo_da_forca()
