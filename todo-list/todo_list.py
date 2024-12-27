# Função para adicionar tarefa
def adicionar_tarefa(tarefa):
    with open("tarefas.txt", "a") as arquivo:
        arquivo.write(tarefa + "\n")
    print(f"Tarefa '{tarefa}' adicionada com sucesso!")

# Função para visualizar as tarefas
def visualizar_tarefas():
    try:
        with open("tarefas.txt", "r") as arquivo:
            tarefas = arquivo.readlines()
            if tarefas:
                print("Tarefas:")
                for i, tarefa in enumerate(tarefas, 1):
                    print(f"{i}. {tarefa.strip()}")
            else:
                print("Nenhuma tarefa encontrada.")
    except FileNotFoundError:
        print("Nenhuma tarefa encontrada.")

# Função para marca uma tarefa como concluída
def marcar_concluida(numero_tarefa):
    try:
        with open("tarefas.txt", "r") as arquivo:
            tarefas = arquivo.readlines()
        
        if 0 < numero_tarefa <= len(tarefas):
            tarefas[numero_tarefa - 1 ] = tarefas[numero_tarefa - 1].strip + " - Concluída\n"
            with open("tarefas.txt", "w") as arquivo:
                arquivo.writelines(tarefas)
            print(f"Tarefa {numero_tarefa} marcada como concluída")
        else:
            print("Número de tarefa inválido.")
    except FileNotFoundError:
        print("Nenhuma tarefa encontrada.")

# Função para excluir uma tarefa
def excluir_tarefa(numero_tarefa):
    try:
        with open("tarefas.txt", "r") as arquivo:
            tarefas = arquivo.readlines()
            
        if 0 < numero_tarefa <= len(tarefas):
            tarefa_removida = tarefas.pop(numero_tarefa - 1).strip()
            with open("tarefas.txt", "w") as arquivo:
                arquivo.writelines(tarefas)
            print(f"Tarefa '{tarefa_removida}' removida com sucesso!")
        else:
            print("Número de tarefa inválido.")
    except FileNotFoundError:
        print("Nenhuma tarefa encontrada.")

# Função principal para interagir com o usuário.
def menu():
    print("\nMenu de Tarefas:")
    print("1. Adicionar tarefa")
    print("2. Visualizar tarefas")
    print("3. Marcar tarefa como concluída")
    print("4. Excluir tarefa")
    print("5. Sair")

def main():
    while True:
        menu()
        escolha = input("Escolha uma opção (1/2/3/4/5): ")

        if escolha == '1':
            tarefa = input("Digite a tarefa: ")
            adicionar_tarefa(tarefa)

        elif escolha == '2':
            visualizar_tarefas()

        elif escolha == '3':
            visualizar_tarefas()
            numero_tarefa = int(input("Digite o número da tarefa a ser marcada como concluída: "))
            marcar_concluida(numero_tarefa)

        elif escolha == '4':
            visualizar_tarefas()
            numero_tarefa = int(input("Digite o número da tarefa a ser excluída: "))
            excluir_tarefa(numero_tarefa)

        elif escolha == '5':
            print("Saindo do programa.")
            break

        else:
            print("Opção inválida, por favor tente novamente.")

# Executar a função principal

if __name__ == "__main__":
    main()


