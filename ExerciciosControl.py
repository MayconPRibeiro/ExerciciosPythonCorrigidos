import this
import ExerciciosModel
this.opcao = -1
this.num1 = -1
this.num2 = -1


def coletarNum1():
    print('Informe um número: ')
    this.num1 = float(input())

def coletarNum2():
    print('Informe mais um número: ')
    this.num2 = float(input())

def Menu():
    print('Menu\n\n' +
        '\n1. Exercicio 01' +
        '\n2. Exercicio 02' +
        '\n3. Exercicio 03' +
        '\n4. Exercicio 04' +
        '\n5. Exercicio 05' +
        '\n6. Exercicio 06' +
        '\n7. Exercicio 07' +
        '\n8. Exercicio 08' +
        '\n9. Exercicio 09' +
        '\n10. Exercicio 10' +
        '\n11. Exercicio 11' +
        '\n12. Exercicio 12' +
        '\n13. Exercicio 13' +
        '\n14. Exercicio 14' +
        '\n15. Exercicio 15' +
        '\n16. Exercicio 16' +
        '\n17. Exercicio 17' +
        '\n18. Exercicio 18' +
        '\n19. Exercicio 19' +
        '\n20. Exercicio 20' +
        '\n0. Sair' +
        '\nEscolha uma das opções acima: ')
    this.opcao = int(input())


def Executar():
    while(this.opcao != 0):
        Menu()
        if this.opcao == 0:
            print('Obrigado')

        elif this.opcao == 1:
            print(ExerciciosModel.exercicio01())

        elif this.opcao == 2:
            coletarNum1()
            print('O antecessor de {} é {}' .format(this.num1, ExerciciosModel.exercicio02(this.num1)))

        elif this.opcao == 3:
            while this.num1<=0:
                print('Informe a base do retângulo em cm')
                this.num1 = float(input())
                if this.num1 <=0:
                    print('Digite um valor positivo')
            while this.num2<=0:
                print('Informe a altura do retângulo em cm')
                this.num2 = float(input())
                if this.num2<=0:
                    print('Digite uma altura positiva')

            print('a área do retângulo é {} cm' .format(ExerciciosModel.exercicios03(this.num1, this.num2)))

        elif this.opcao == 4:
            print('Digite o ano de nascimento')
            this.ano = int(input())
            print('Digite o mes do seu nascimento')
            this.mes = int(input())
            print('Digite o dia do seu nascimento')
            this.dia = int(input())
            print('Você contém atualmente {} dias de vida' .format(ExerciciosModel.exercicios04(this.ano, this.mes, this.dia)))

        elif this.opcao == 5:
            print('Digite o total de votos brancos')
            this.brancos = int(input())
            print('Digite o total de votos nulos')
            this.nulos = int(input())
            print('Digite o total de votos válidos')
            this.validos = int(input())

            print(ExerciciosModel.exercicios05(this.brancos, this.nulos, this.validos))

        elif this.opcao == 6:
            print(ExerciciosModel.exercicio06())

        elif this.opcao == 7:
            print(ExerciciosModel.exercicio07())

        elif this.opcao == 8:
            print(ExerciciosModel.exercicio08())

        elif this.opcao == 9:
            print(ExerciciosModel.exercicio09())

        elif this.opcao == 10:
            print(ExerciciosModel.exercicio10())

        elif this.opcao == 11:
            print(ExerciciosModel.exercicio11())

        elif this.opcao == 12:
            print(ExerciciosModel.exercicio12())

        elif this.opcao == 13:
            print(ExerciciosModel.exercicio13())

        elif this.opcao == 14:
            print(ExerciciosModel.exercicio14())

        elif this.opcao == 15:
            print(ExerciciosModel.exercicio15())

        elif this.opcao == 16:
            print(ExerciciosModel.exercicio16())

        elif this.opcao == 17:
            print(ExerciciosModel.exercicio17())

        elif this.opcao == 18:
            print(ExerciciosModel.exercicio18())

        elif this.opcao == 19:
            print(ExerciciosModel.exercicio19())

        elif this.opcao == 20:
            print(ExerciciosModel.exercicio20())

        else:
            print('Opção informada não é válida')