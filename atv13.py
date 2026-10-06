#Declare uma variável representando a velocidade de um carro e uma constante LIMITE_VELOCIDADE representando 
#o limite da via. Utilizando o operador lógico  NÃO, exiba se o motorista não está cometendo infração, 
# ou seja, se sua velocidade não ultrapassa o limite permitido. 

velocidade = 300.0
LIMITE_VELOCIDADE = 350.0
naoCometInfra = (not velocidade > LIMITE_VELOCIDADE)
print("Este motorista não está cometendo uma infração? ", naoCometInfra)


