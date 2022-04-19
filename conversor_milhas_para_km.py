from tkinter import *

FONTE = ("Courier", 15, "normal")

tela = Tk()
tela.title("Conversor Milhas para KMs")
tela.configure(padx=20, pady=20)

# Componente de entrada de dados
entrada_de_dados = Entry(width=10, font=FONTE, justify="center")
entrada_de_dados.insert(END, string="0")
entrada_de_dados.grid(row=0, column=1)


def criar_componente_texto(text, row, column):
	texto = Label(text=f"{text}", font=FONTE)
	texto.grid(row=row, column=column)
	texto.configure(padx=10, pady=10)
	return texto


def converter_milhas_para_kms():
	dados_capturados = float(entrada_de_dados.get())
	milhas_para_kms = round(dados_capturados * 1.609344, 2)
	texto_km.configure(text=milhas_para_kms)


# Componente de Texto
criar_componente_texto(text="Milhas", row=0, column=2)

# Componente de Texto
criar_componente_texto(text="É igual a", row=1, column=0)

# Componente de Texto
texto_km = criar_componente_texto(text=0, row=1, column=1)

# Componente de Texto
criar_componente_texto("Kms", row=1, column=2)

# Componente Botão
botao_calcular = Button(text="Calcular", font=FONTE, command=converter_milhas_para_kms)
botao_calcular.grid(row=2, column=1)
botao_calcular.configure(padx=10, pady=5)

tela.mainloop()
