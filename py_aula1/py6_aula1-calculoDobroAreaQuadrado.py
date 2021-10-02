'''
Foi solicitado uma aplicação que calculasse a área de um quadrado
e, em seguida, imprima o dobro do valor dessa área para o usuário.
'''
ladoA = float(input("Informe qual o tamanho do 1° lado do seu quadrado: "));
ladoB = float(input("Informe qual o tamanho do 2° lado do seu quadrado: "));
area = (ladoA * ladoB);

print("")
print("A área calculada equivale a {:.2f}m².".format(area));
print("O dobro da área calculada equivale a {:.2f}m²".format(area*2));

#Foi solicitado pelo professor que a parte fracionária do resultado
#não fosse maior que duas casas decimais. Para isso foi usado a função
#".format()".
