'''
Esta aplicação solicita ao usuário dois valores quaisquer
via teclado, armazena e soma esses valores e logo após
NEWS.txt
'''

valor1 = float(input("Informe o seu primeiro valor: "));
valor2 = float(input("Informe o seu segundo valor: "));
soma = valor1 + valor2;

print("O resultado da sua soma = {:.2f}.".format(soma));
