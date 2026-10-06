#Declare três variáveis booleanas representando se uma pessoa possui os documentos RG, CPF e comprovante de 
#residência. Utilizando o operador lógico E, exiba se a pessoa possui toda a documentação necessária para realizar um 
#cadastro. 

possuiRg = True
possuiCpf = True
possuiCompRes = True
# Alternativamente, a sentença posterior pode ser declarada como:
# podeReaCad = possuiRg and possuiCpf and possuiCompRes
podeReaCad = (possuiRg == True) and (possuiCpf == True) and (possuiCompRes == True)
print("Esta pessoa está apta a realizar um cadastro? ", podeReaCad)
