def ler_notas():
    n = float(input("Digite a nota do aluno(a):"))
    return n


def resultado(n1, n2):
    media = (n1+n2)/2
    print("Nota 1:", n1)
    print("Nota 2:", n2)
    print("Media: ", media, "Resultado:", end="")
    if media >= 7:
        print("Aprovado!")
    else:
        print("Reprovado!")


a = ler_notas()
b = ler_notas()
resultado(a, b)