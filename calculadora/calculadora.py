def adicionar(x, y):
    return x + y

def subtrair(x, y):
    return x - y

def multiplicar(x, y):
    return x * y

def dividir(x, y):
    if y !=0:
        return x/ y
    else:
        return "Erro! Divisão de zero."
    
def calculadora():
    print("Selecione a operação")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")

    while True:
        # Recebe a escolha do usuário
        escolha = input("Digite sua escolha (1/2/3/4): ")

        # Verifica se a escolha é válida
        if escolha in ['1', '2', '3', '4']:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))

            if escolha == '1':
                print(f"{num1} + {num2} = {adicionar(num1, num2)}")

            if escolha == '2':
                print(f"{num1} - {num2} = {subtrair(num1, num2)}")

            if escolha == '3':
                print(f"{num1} * {num2} = {multiplicar(num1, num2)}")

            if escolha == '4':
                print(f"{num1} / {num2} = {dividir(num1, num2)}")
            
            # verifica se o usuário deseja continuar
            proxima_operacao = input("Deseja realizar outra operação? (s/n): ")
            if proxima_operacao.lower() != 's':
                break
            else:
                print("Escolha Inválida, por favor tente novamente.")
                print(50*"-")
if __name__ == "__main__":
    calculadora()