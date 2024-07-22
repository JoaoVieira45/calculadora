from tkinter import *                                                       #importa o tkinter, o * é para importar tudo do tkinter
def somar():                                                                #função para soma
    print('somar')
    if(str(ent_n1.get()).isnumeric() and str(ent_n2.get()).isnumeric()):    #verifica se os valores são númericos
        n1 = int(ent_n1.get())
        n2 = int(ent_n2.get())
        lb['text'] = n1 + n2
    else:
        lb['text'] = 'Valores informados são inválidos'                     #caso não for, imprimi uma mensagem de erro

janela = Tk()                                                               #inicia a janela
janela.title('Calculadora')                                                 #muda o titulo da janela
text_orient = Label(janela, text = 'O que deseja calcular?')
text_orient.grid(column = 0, row = 0)
text_n1 = Label(janela, text = 'Primerio número')                           #janela de entrada
text_n1.grid(column = 0, row = 1)
ent_n1 = Entry(janela, width = 10)
ent_n1.grid(column = 1, row = 1)
text_n2 = Label(janela, text = 'Segundo número')
text_n2.grid(column = 0, row = 2)
ent_n2 = Entry(janela, width = 10)
ent_n2.grid(column = 1, row = 2)
bt_soma = Button(janela, text = 'Soma', command = somar)                    #botão para executar a função soma
bt_soma.grid(column = 0, row = 3)
lb = Label(janela, text = '0')
lb.grid(column = 1, row = 4)
janela.mainloop()                                                           #deixa a janela sempre aberta



#código inicial da calculadora se manterá por enquanto
#while True:
#    print('-'*20)
#    resp = int(input('O que deseja calcular?\n[1]Soma\n[2]Subtração\n[3]Divisão\n[4]Multiplicação\nR:'))
#    n1 = float(input('Digite o primeiro número: '))
#    n2 = float(input('Digite o segundo número: '))
#    def soma()
#    if resp == 1:
#        soma = n1 + n2
#        print(f'A soma de {n1} com {n2} é {soma}')
#    if resp == 2:
#        soma = n1 - n2
#        print(f'A subtração de {n1} com {n2} é {soma}')
#    if resp == 3:
#        soma = n1 / n2
#        print(f'A divisão de {n1} com {n2} é {soma}')
#    if resp == 4:
#        soma = n1 * n2
#        print(f'A multiplicação de {n1} com {n2} é {soma}')
#    print('-'*20)
#    cont = str(input('Deseja continuar?s/n ')).strip().lower()
#    if cont in 'naon':
#        break
#      print('-'*20)

