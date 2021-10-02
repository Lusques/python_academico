'''
Este programa calcula a área de um círculo, com base no valor do raio.
Logo após efetuar o cálculo, ele mostra o resultado na tela.
Área = π x raio².
'''

import math;

raio = float(input("Informe o raio do seu círculo(m): "));
areaDoCirculo = (math.pi * raio**2);
print("O raio do círculo com raio ", raio, " equivale a {:.3f}".format(areaDoCirculo),"m²")
#Foi solicitado pelo professor que o resultado utilizasse até
#três casas decimais após a vírgula, foi usado a função ".format()"
#para limitar e arredondar a parte fracionária da resultado.
