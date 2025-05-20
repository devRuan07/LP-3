numeroParaFatorar = int(input("Digite um numero:"))

i = 1
fatorial = 1
while i <= numeroParaFatorar:
    fatorial = (i * fatorial)
    i += 1
print(f"{fatorial}, é valor do fatorial que você digitou do numero {numeroParaFatorar}!")