from tkinter import *

class Calculadora(object):
    def __init__(self, janela):
        #Frame que contem os checkbuttons
        self.frame1 = Frame(janela)

        #Frame que contem a entrada de texto
        self.frame2 = Frame(janela)

        #Frame que contem o botão calcular
        self.frame3 = Frame(janela)

        #Frame que contem o texto das formulas
        self.frame4 = Frame(janela, pady = 20)

        #Frame que contem os botões especificos
        self.frame5 = Frame(janela)

        #Empacotamos as nossas frames
        self.frame1.pack()
        self.frame2.pack()
        self.frame3.pack()
        self.frame4.pack()
        self.frame5.pack()

        #Colocar a entrada de texto
        self.form = Entry(self.frame2)
        self.form.pack()

        #Botão calcular
        self.calc = Button(self.frame3, text = "Calcule", command = self.Calcular)
        self.calc.pack()

        #Texto das formulas
        self.resultado = Label(self.frame4, text ="Resultado", fg = "red")
        self.resultado.pack()

        botões = ('Comb(n, k)', 'binomial(n, x, p)', 'poisson(l, x, t)', 'soma(n, p, maior, menor = 0)', 'media', 'desvio', 'moda', 'mediana', 'variancia', 'p(x > k)', 'p(x >= k)', 'p(x < k)', 'p(x <= k)', 'p(k1 < x < k2)', 'p(k1 <= x < k2)', 'p(k1 < x <= k2)', 'p(k1 <= x <= k2)')
        botoes = ( "1", "2", "3", "4", "5", "6", "7", "8","9","10", "11", "12", "13", "14", "15"," ")

        for i in range(len(botoes)):
            if i % 4 == 0:
                 subframe = Frame(self.frame5)
                 subframe.pack()
            a = Button(subframe, text = botoes[i], bg = 'green', width =4, padx = 5, fg = "yellow")
            a.pack(side = LEFT)

        #self.delete = Button(subframe, text = 'del', bg = 'red', width = 25, padx = 5)
        #self.delete.pack(side = LEFT)

    def Calcular(self):
        self.resultado['text'] = self.form.get()
        self.resultado['fg'] = 'green'

#Cria a nossa tela
janela = Tk()

#Criamos uma janela da calculadora
Calculadora(janela)

#Dá um título a tela
janela.title('Jogo Quebra Cabeças Numérico')

#Dá um tamanho a tela
janela.geometry("800x600")

#Dá um ícone ao aplicativo
#janela.wm_iconbitmap('icone.ico')

#Inicia o programa
janela.mainloop()
