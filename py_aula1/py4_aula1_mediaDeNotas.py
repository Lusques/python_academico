'''
Esta aplicacão tem o intuito de pedir 4 notas de um aluno e calcular
a média dessas notas, mostrando o resultado na tela em seguida.
'''


nota1 = float(input("Informe o valor da sua 1° nota: "));
nota2 = float(input("Informe o valor da sua 2° nota: "));
nota3 = float(input("Informe o valor da sua 3° nota: "));
nota4 = float(input("Informe o valor da sua 4° nota: "));
media = (nota1 + nota2 + nota3 + nota4)/4;


print("A média das suas notas equivale a {:.2f}".format(media));
