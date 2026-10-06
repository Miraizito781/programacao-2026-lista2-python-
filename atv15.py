#Declare  duas  variáveis  representando  a  idade  de  duas  pessoas  e  uma  constante  IDADE_MINIMA
# com  valor  18. Utilizando os operadores lógicos E e OU combinados, exiba se pelo menos uma delas é
# maior de idade e, simultaneamente, se a soma das idades das duas pessoas é superior a 40 anos.

idade1 = 50
idade2 = 45
IDADE_MINIMA = 18
#Em python, and é avaliado antes de or. Os parênteses agrupam o OR antes de combinar o resultado com AND.
result = ((idade1 >= IDADE_MINIMA) or (idade2 >= IDADE_MINIMA)) and (idade1 + idade2 > 40)
print("Ao menos uma dessas pessoas é maior de idade? A soma de idade delas ultrapassa os 40? ", result, )


