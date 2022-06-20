

def exercicio01():

    a = 10
    b = 20
    msg = "Antes da troca A = {} e B = {}" .format(a, b)
    aux = a
    a = b
    b = aux
    msg = msg + "\nDepois da troca A = {} e B = {}" .format(a, b)
    return msg

def exercicio02(num1):

    return num1 - 1

def exercicios03(num1, num2):

    return num1 * num2

def exercicios04(ano, mes, dia):

    anod = (2022 - ano) * 365
    mesd = mes * 30
    diad = dia

    total = anod + mesd + diad
    return total

def exercicios05(brancos, nulos, validos):

    totalv = brancos + nulos + validos

    brancosP = (brancos/totalv)*100
    nulosP = (nulos/totalv)*100
    validosP = (validos/totalv)*100

    msg = '{}% Votos brancos, {}% Votos nulos e {}% Votos válidos' .format(brancosP, nulosP, validosP)
    return msg

def exercicio06():
    salario = float(input('Informe o salário em R$:'))
    reajuste = float(input('Informe a porcentagem do reajuste:'))
    novosalario = ((reajuste/100)*salario)+ salario

    print ('Seu novo salário será R${}' .format(novosalario))

def exercicio07():
    custo = float(input('Informe o custo de fábrica em R$: '))
    dist = (28/100)*custo
    imp = (45/100)*custo
    consu = custo + imp + dist

    print('O valor final será R${}' .format(consu))

def exercicio08():
    nota1 = float(input('Primeira nota: '))
    nota2 = float(input('Segunda nota: '))
    nota3 = float(input('Terceira nota: '))

    media = (nota1+nota2+nota3)/3

    print ('A nota média foi {}' .format(media))

def exercicio09():
    maca = int(input('Digite o número de maçãs que deseja comprar: '))
    if maca < 12:
        total = maca*1.30
        print ('O valor de {} maçã(s) ficou em R${}'.format(maca, total))
    else:
        total = maca*1
        print('O valor de {} maçã(s) ficou em R${}' .format(maca, total))

def exercicio10():
    n1 = int(input('Digite um número: '))
    n2 = int(input('Digite outro número: '))
    n3 = int(input('Digite outro número: '))
    n4 = int(input('Digite outro número: '))
    n5 = int(input('Digite outro número: '))
    n6 = int(input('Digite outro número: '))
    n7 = int(input('Digite outro número: '))
    n8 = int(input('Digite outro número: '))
    n9 = int(input('Digite outro número: '))
    n10 = int(input('Digite outro número: '))
    lista = n1, n2, n3, n4, n5, n6, n7, n8, n9, n10
    for i in lista:
        return sorted(lista)

def exercicio11():
    salario = float(input('Digite seu salário fixo em R$:'))
    vendas = float(input('Digite o total das suas vendas em R$: '))
    if vendas >= 1500.0:
            c5 = (5*(vendas-1500))/100
            c3 = (3*vendas)/100
            total = salario+c3+c5

            return 'Parabéns, além do comissionamento de 3%, você atigiu o bônus de 5%, seu salário total será R${}'.format(total)
    else:
            c3 = (3/vendas)*100
            total = salario + c3

            return 'Seu salário total será R${}'.format(total)

def exercicio12():
    conta = int(input('Digite o número da sua conta:'))
    saldo = float(input('Digite seu saldo em R$:'))
    debito = float(input('Digite o débito que você possui em R$:'))
    credito = float(input('Digite o seu crédito em R$:'))

    saldoatual = saldo - debito + credito
    if saldoatual >= 0:
        return 'Saldo Positivo, seu saldo atual é de R${}'.format(saldoatual)

    else:
        return 'Saldo Negativo, seu saldo atual é de -R${}' .format(saldoatual)

def exercicio13():
    n = int(input('Digite um valor entre 1 e 10: '))
    if n > 10:
        return 'Opção inválida, digite um valor entre 1 e 10'
    elif n<0:
        return 'Opção inválida, digite um valor entre 1 e 10'
    else:
        for i in range(1, 11):
            resultado = n*i
            print('{} * {} = {}'.format(n, i, resultado))

def exercicio14():
    n = int(input('Digite um número: '))
    for i in range(1, n+1):
        print(i)

def exercicio15():
    lista = 0
    for i in range(1,11):
        n = int(input('Digite um número: '))
        if n<0:
            lista += +1

    print('Sua lista possui {} números negativos' .format(lista))

def exercicio16():
    lista = 0
    for i in range(1, 11):
        n = float(input('Digite um número: '))
        if n<40:
            lista += n

    print('O resultado da sua soma é {}' .format(lista))

def exercicio17():
    aux = 0
    quantidade = 0
    for i in range(1, 101):

        aux += i
        quantidade += +1
        result = aux/quantidade

    print('{} / {} = {}' .format(aux, quantidade, result))

def exercicio18():
   n = int(input('Quantos números deseja digitar? '))
   if n<=0:
       print('Obrigado!')
   else:
    aux3 = 0
    quantidade = 1

    maior = float(input('Digite um número: '))
    for i in range(2, n + 1):
        num = float(input('Digite um número: '))

        aux2 = maior
        aux3 += num
        quantidade += +1
        media = (aux2+aux3)/quantidade

        if num>maior:
            maior = num

    print ('O maior número digitado foi {}'.format(maior))
    print('A média dos números digitados foi {}' .format(media))

def exercicio19():
    total = 0
    maior = 0
    lista = []
    for i in range(20):
        notas = float(input('Digita sua nota de 0 a 10: '))
        lista.append(notas)
        if notas>10:
            print('Digite uma nota válida')
        elif notas<0:
            print('Digite uma nota válida')
        else:
            total += notas
            mediag = total / 20

    for i in range(20):
       if lista[i] > mediag:
          maior += 1

    print('A média da turma foi {}.'.format(mediag))
    print('{} aluno(s) tiveram nota maior que a média'.format(maior))

def exercicio20():
    medias = 0
    mediaf = 0
    aux = 0
    abaixo = 0

    habitantes = int(input('Digite a quantidade de habitantes: '))
    for i in range(1, habitantes+1):
        salario = float(input('Digite seu salário em R$: '))
        if salario<=150.0:
            abaixo = +1
        if aux<salario:
            aux = salario
        if salario<0:
            print('Salário inválido')
        filhos = int(input('Digite a quantidade de filhos que você possui: '))
        if filhos<0:
            print('Quantidade inválida')

        medias += salario
        mediaf += filhos
    results = medias/habitantes
    resultf = mediaf/habitantes
    resultmenor = (abaixo/habitantes)*100

    print('Média do salário da população R$:{}' .format(results))
    print('Média número de filhos por habitante: {}' .format(resultf))
    print('Maior salário dos habitantes, R$:{}'.format(aux))
    print('Há {}% de pessoas com salário abaixo de R$150.0'.format(resultmenor))



