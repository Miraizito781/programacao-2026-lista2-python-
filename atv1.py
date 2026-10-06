# .lower() deixa o texto em letras minúsculas
carteira = input("Você possui carteira de motorista?").lower()
idade = int(input("Quantos anos você tem?"))
tem_carteira = carteira == "sim"
maiordeIdade = idade >= 18
apto_dirigir = tem_carteira and maiordeIdade
print("A pessoa está apta a dirigir ?" , apto_dirigir)
