qtd = 0
soma = 0
media = 0
valor = float(input("Digite um valor:"))

while valor > 0.0:
    soma = soma + valor
    qtd = qtd + 1

    valor = float(input("Digite um valor ou qualquer valor negativo para finalizar:"))

media = soma / qtd
print("\nTotal de soma:", soma)
print("\nQuantidade de numeros digitados:", qtd)
print("\nA média dos valores é:", media)
