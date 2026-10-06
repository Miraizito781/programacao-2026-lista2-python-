# Declare  uma  variável  representando  o  horário  atual  (em  formato  de  hora,  por  exemplo,  22)  e
# duas  constantes representando o início e o fim do expediente comercial: 
#INICIO_EXPEDIENTE = 8 
#FIM_EXPEDIENTE = 18
#Utilizando o operador lógico NÃO combinado com o operador E, exiba se o horário informado está f
#ora do expediente 
#comercial. 

horarioAtual = 22
INICIO_EXPEDIENTE = 8
FIM_EXPEDIENTE = 18
horarioComercial = (horarioAtual >= INICIO_EXPEDIENTE) and (horarioAtual <= FIM_EXPEDIENTE)
print("O horário atual está fora do horário comercial? ", not horarioComercial)