from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox

# funcoes


def validar(nomeBase, quantidadeBase, precoBase, geladoBase):
    booleano = True
    if nomeBase == "" or nomeBase == " ":
        messagebox.showerror(title="Erro", message="Digite um nome!")
        booleano = False
    elif (
        quantidadeBase == ""
        or quantidadeBase == " "
        or quantidadeBase.isnumeric() == False
    ):
        messagebox.showerror(title="Erro", message="Digite um número na quantidade!")
        booleano = False
    elif precoBase == "" or precoBase == " " or precoBase.isnumeric() == False:
        messagebox.showerror(title="Erro", message="Digite um número no preço!")
        booleano = False
    elif geladoBase == "" or geladoBase == " ":
        messagebox.showerror(
            title="Erro", message="Selecione uma opção da caixa de seleções!"
        )
        booleano = False
    if booleano == True:
        escreverProdutos()
    else:
        pass


def escreverProdutos():
    nomeBase = inputNome.get()
    quantidadeBase = inputQuantidade.get()
    precoBase = inputPreco.get()
    geladoBase = inputCampo.get()
    arquivo = open("estoque.txt", "a", encoding="utf-8")
    arquivo.write(f"{nomeBase},{quantidadeBase},{precoBase},{geladoBase}\n")
    arquivo.close()


def verProdutos():
    windowTwo = Tk()
    windowTwo.title("Produtos")
    windowTwo.geometry("1280x720")
    arquivo = open("estoque.txt", "r", encoding="utf-8")
    for linha in arquivo.readlines():
        produto = linha.split(",")
        labelProduto = Label(
            windowTwo,
            text=f"Nome: {produto[0]} | Quantidade: {produto[1]} | Preço: {produto[2]} | Gelado: {produto[3]}",
        )
        labelProduto.pack()
    arquivo.close()


def limparFormulario():
    inputNome.delete(0, END)
    inputQuantidade.delete(0, END)
    inputPreco.delete(0, END)
    inputCampo.delete(0, END)


# gui

window = Tk()
window.title("Sistema de Controle de Estoque")
window.geometry("600x300")

# nome

labelNome = Label(window, text="Nome:")
labelNome.pack()
inputNome = Entry(window, bd=2)
inputNome.pack()

# quantidade em estoque

labelQuantidade = Label(window, text="Quantidade em estoque:")
labelQuantidade.pack()
inputQuantidade = Entry(window, bd=2)
inputQuantidade.pack()

# preço unitáro

labelPreco = Label(window, text="Preço unitário:")
labelPreco.pack()
inputPreco = Entry(window, bd=2)
inputPreco.pack()

# campo de seleção

labelCampo = Label(window, text="Gelado ou Não?")
labelCampo.pack()
values = ("Sim", "Não")
inputCampo = Combobox(window, values=values)
inputCampo.pack()

# botões

botaoAdicionar = Button(
    window,
    text="Adicionar",
    command=lambda: validar(
        inputNome.get(), inputQuantidade.get(), inputPreco.get(), inputCampo.get()
    ),
)
botaoAdicionar.pack()
botaoLimpar = Button(window, text="Limpar Formulário", command=limparFormulario)
botaoLimpar.pack()
botaoVisualizar = Button(window, text="Visualizar Produtos", command=verProdutos)
botaoVisualizar.pack()

window.mainloop()
