#Declare uma variável representando a nota de um aluno e uma variável booleana indicando se ele entregou todos 
#os  trabalhos.  Combine  os  operadores  lógicos  E  e 
#NÃO  para  exibir  se  o  aluno  está  em  situação  de  recuperação, 
#considerando que sua nota é menor que a média mínima e que ele não entregou todos os trabalhos.

nota = 5.0
MEDIA_MINIMA = 7.0
entregouTrab = False
recuperacao = (nota < MEDIA_MINIMA) and (not entregouTrab == True)
print("Este aluno está em recuperação? ", recuperacao)


