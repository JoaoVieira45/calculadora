from tkinter import *                                                       #importa o tkinter, o * é para importar tudo do tkinter
def somar():                                                                #função para soma
    print('Soma')
    if(str(ent_n1.get()).isnumeric() and str(ent_n2.get()).isnumeric()):    #verifica se os valores são númericos
        n1 = int(ent_n1.get())
        n2 = int(ent_n2.get())
        lb['text'] = n1 + n2
    else:
        lb['text'] = 'Valores inválidos'                     #caso não for, imprimi uma mensagem de erro
def sub():                                                                  #função para subtração
    print('SubTração')
    if (str(ent_n1.get()).isnumeric() and str(ent_n2.get()).isnumeric()):
        n1 = int(ent_n1.get())
        n2 = int(ent_n2.get())
        lb['text'] = n1 - n2
    else:
        lb['text'] = 'Valores inválidos'

def multi():                                                                #função para multiplicação
    print('Multiplicação')
    if (str(ent_n1.get()).isnumeric() and str(ent_n2.get()).isnumeric()):
        n1 = int(ent_n1.get())
        n2 = int(ent_n2.get())
        lb['text'] = n1 * n2
    else:
        lb['text'] = 'Valores inválidos'

def divi():                                                                 #função para divisão
    print('Divisão')
    if (str(ent_n1.get()).isnumeric() and str(ent_n2.get()).isnumeric()):
        n1 = int(ent_n1.get())
        n2 = int(ent_n2.get())
        lb['text'] = n1 / n2
    else:
        lb['text'] = 'Valores inválidos'

janela = Tk()                                                               #inicia a janela
janela.geometry('300x250')
janela.title('Calculadora')                                                 #muda o titulo da janela
text_orient = Label(janela, text = 'O que deseja calcular?')                #.place, movo o objeto livremente pela tela, utilizando x e y
text_orient.place(x = 75, y = 20)                                           #.grid, janela dividida em colunas e coloco o objeto dentro dessas colunas, utilizando column e row
text_n1 = Label(janela, text = 'Primerio número')                           #janela de entrada
text_n1.place(x = 50, y = 60)
ent_n1 = Entry(janela, width = 10)
ent_n1.place(x = 160, y = 60)
text_n2 = Label(janela, text = 'Segundo número')
text_n2.place(x = 48, y = 80)
ent_n2 = Entry(janela, width = 10)
ent_n2.place(x = 160, y = 80)
bt_soma = Button(janela, text = 'Soma', command = somar)                    #botão para executar a função soma()
bt_soma.place(x = 75, y = 105)
bt_sub = Button(janela, text = 'SubTração', command = sub)                  #botão para executar a função sub()
bt_sub.place(x = 64, y = 133)
bt_multi = Button(janela, text = 'Multiplicação', command = multi)          #botão para executar a função multi()
bt_multi.place(x = 56, y = 161)
bt_divi = Button(janela, text = 'Divisão', command = divi)                  #botão para executar a função divi()
bt_divi.place(x = 73, y = 189)
lb = Label(janela, text = '0')
lb.place(x = 184, y = 100)
janela.mainloop()                                                           #deixa a janela sempre aberta
