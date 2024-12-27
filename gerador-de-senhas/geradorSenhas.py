import tkinter as tk
from tkinter import messagebox
import random
import string

def gerar_senha():
    try:
        # Obter o comprimento da senha
        comprimento = int(entrada_comprimento.get())
        if comprimento < 4:
            raise ValueError("O comprimento mínimo é 4.")

        # Verificar as opções de caracteres
        caracteres = ""
        if var_letras_maiusculas.get():
            caracteres += string.ascii_uppercase
        if var_letras_minusculas.get():
            caracteres += string.ascii_lowercase
        if var_numeros.get():
            caracteres += string.digits
        if var_simbolos.get():
            caracteres += string.punctuation
        
        if not caracteres:
            raise ValueError("Selecioine pelo menos uma categoria de caracteres.")
        
        # Gerar a senha

        senha = "".join(random.choice(caracteres) for _ in range(comprimento))
        senha_exibida.delete(0, tk.END)
        senha_exibida.insert(0, senha)
    except ValueError as e:
        messagebox("Error", str(e))

# Configuração da janela principal
janela = tk.Tk()
janela.title("Gerador de Senhas")
janela.geometry("400x300")

#Título do programa
titulo = tk.Label(janela, text="Gerador de Senhas", font=("arial", 16, "bold"))
titulo.pack(pady=10)

# Campo para selecionar o comprimento da senha
frame_comprimento = tk.Frame(janela)
frame_comprimento.pack(pady=5)

tk.Label(frame_comprimento, text="Comprimento da Semha:", font=("Arial, 12")).pack(side="left")

entrada_comprimento = tk.Entry(frame_comprimento, font=("Arial, 12"), width=5)
entrada_comprimento.pack(side="left", padx=5)

# Opções de caracteres
var_letras_maiusculas = tk.BooleanVar(value=True)
var_letras_minusculas = tk.BooleanVar(value=True)
var_numeros = tk.BooleanVar(value=True)
var_simbolos = tk.BooleanVar(value=False)

tk.Checkbutton(janela, text="Letras maiúsculas", variable=var_letras_maiusculas, font=("Arial", 12)).pack(anchor="w")
tk.Checkbutton(janela, text="Letras minúscilas", variable=var_letras_minusculas, font=("Arial", 12)).pack(anchor="w")
tk.Checkbutton(janela, text="Números", variable=var_numeros, font=("Arial", 12)).pack(anchor="w")
tk.Checkbutton(janela, text="Símbolos", variable=var_simbolos, font=("Arial", 12)).pack(anchor="w")

# Botão para gerar senha
botao_gerar = tk.Button(janela, text="Gerar Senha", command=gerar_senha, font=("Arial", 12,))
botao_gerar.pack(pady=20)

# Campo para exibir a senha gerada
senha_exibida = tk.Entry(janela, font=("Arial", 12), justify="center")
senha_exibida.pack(pady=10)

janela.mainloop()
