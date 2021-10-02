'''
Esta aplicação tem o intuito de converter um valor dado
pelo usuário em metros, para o mesmo valos, mas na unidade
de medida de centímetros e, logo após mostrar o resultado
para o usuário.
'''

entradaMetros = float(input("Informe uma medida em metros: "));
centimetros = entradaMetros * 100;

print("")
print("{:.2f}m = {:.2f}cm.".format(entradaMetros, centimetros));
