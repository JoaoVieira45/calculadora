while True:
    print('-'*20)
    resp = int(input('O que deseja calcular?\n[1]Soma\n[2]Subtração\n[3]Divisão\n[4]Multiplicação\nR:'))
    if resp == 1:
        n1 = float(input('Digite o primeiro número: '))
        n2 = float(input('Digite o segundo número: '))
        soma = n1 + n2
        print(f'A soma de {n1} com {n2} é {soma}')
    if resp == 2:
        n1 = float(input('Digite o primerio número: '))
        n2 = float(input('Digite o segundo número: '))
        soma = n1 - n2
        print(f'A subtração de {n1} com {n2} é {soma}')
    if resp == 3:
        n1 = float(input('Digite o primerio número: '))
        n2 = float(input('Digite o segundo número: '))
        soma = n1 / n2
        print(f'A divisão de {n1} com {n2} é {soma}')
    if resp == 4:
        n1 = float(input('Digite o primeiro número: '))
        n2 = float(input('Digite o segundo número: '))
        soma = n1 * n2
        print(f'A multiplicação de {n1} com {n2} é {soma}')
    print('-'*20)
    cont = str(input('Deseja continuar?s/n ')).strip().lower()
    if cont in 'naon':
        break
    print('-'*20)