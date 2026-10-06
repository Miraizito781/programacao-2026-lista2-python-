#Declare duas variáveis representando a quantidade em estoque de dois produtos diferentes em uma loja.
# Utilizando 
#o operador lógico OU, exiba se pelo menos um dos produtos está em falta (estoque igual a zero).

qtdProd1 = 0
qtdProd2 = 0
emFalta = (qtdProd1 == 0) or (qtdProd2 == 0)
print("Algum desses produtos está em falta? ", emFalta)
