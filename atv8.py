possuiCadastro = True
possuiCupom = True
# alternativamente, pode-se fazer na próxima linha = podeBeneficio = possuiCadastro or possuiCupom
podeBeneficio = (possuiCadastro == True) or (possuiCupom == True) 
print("Esse cliente pode receber algum beneficio na loja? " , podeBeneficio)