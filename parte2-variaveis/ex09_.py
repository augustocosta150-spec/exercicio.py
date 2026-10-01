nota01 = float(input("Digite a primeira nota:"))
nota02 = float(input("Digite a segunda nota:"))
nota03 = float(input("Digite a terceira nota:"))

medianota = (nota01 + nota02 + nota03)/3

if medianota >= 6:
    print("Aluno aprovado.")
elif medianota >= 4:
    print("Aluno precisa de recuperação:")
else:
    print("Aluno reprovado")