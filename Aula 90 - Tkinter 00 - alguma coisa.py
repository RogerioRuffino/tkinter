from tkinter import *
def dolar(): print ("abrir")
def prox_venc(): print ("salvar")
def graficos() : print ("ajuda")

def fornecedores(): print ("Fortilizantes")
def produtores(): print ("Produtores")
def Insumos(): print ("Insumos")
def sementes(): print ("Sementes")
def defensivos() : print ("Defensivos")
def outros(): print ("Defensivo")

root=Tk()
root.geometry('1000x720')
menu=Menu(root)
root.configure(menu=menu)

inicio= Menu(menu)
menu.add_cascade(label="Início",menu=inicio)
inicio.add_command(label="Cotação do dolar", command = dolar)
inicio.add_command(label="Próximos vencimentos",command=prox_venc)
inicio.add_command(label="Gráficos",command=graficos)

cadastro= Menu(menu)
menu.add_cascade(label="Cadastro",menu=cadastro)
cadastro.add_command(label="Fornecedores", command = fornecedores)
cadastro.add_command(label="Produtores",command=produtores)
cadastro.add_command(label="Insumos",command=Insumos)

#insumos.add_cascade(label="Início",insumos=fertilizantes)


commodities= Menu(menu)
menu.add_cascade(label="Commodities",menu=commodities)
commodities.add_command(label="Soja", command = dolar)
commodities.add_command(label="Milho",command=prox_venc)
commodities.add_command(label="Algodao",command=graficos)

negociacao= Menu(menu)
menu.add_cascade(label="Negociacao", menu=negociacao)
negociacao.add_command(label="Safra 19/20", command = dolar)
negociacao.add_command(label="Safra 20/21",command=prox_venc)
negociacao.add_command(label="Safra 21/22",command=graficos)

financeiro= Menu(menu)
menu.add_cascade(label="Contas a Pagar",menu=financeiro)
financeiro.add_command(label="Contas a Receber", command = dolar)
financeiro.add_command(label="Produtores",command=prox_venc)

contabil= Menu(menu)
menu.add_cascade(label="Início",menu=contabil)
contabil.add_command(label="Cotação do dolar", command = dolar)
contabil.add_command(label="Próximos vencimentos",command=prox_venc)

sistema= Menu(menu)
menu.add_cascade(label="Usuário",menu=sistema)
sistema.add_command(label="Configuração", command = dolar)

menu.mainloop()
