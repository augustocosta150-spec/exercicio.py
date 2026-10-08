num = 1
par = 0
impar = 0
while num != 0:
    num = int(input("Digite um numero: "))
    if num != 0:
        if num %2 == 0:
            par = par + 1
        else:
            impar = impar + 1
print(f"Quantidade de números pares: {par}")
print(f"Quantidade de números ímpares: {impar}")