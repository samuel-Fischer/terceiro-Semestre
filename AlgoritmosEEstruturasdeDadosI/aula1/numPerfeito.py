# 7. Um número é dito perfeito, quando é igual a soma dos seus divisores (exceto com o próprio número). Ler
# um número, exibir os seus divisores e informar se ele é ou não perfeito.

num = int(input("Numero: "))
divi = []
soma = 0

for i in range(1,num,+1):
  if num % i == 0:
    divi.append(i)

divisores = ", ".join(str(elemento) for elemento in divi)

for i in range(len(divi)):
  soma = soma+int(divi[i])

print(f"divisores do {num}: {divisores}")
if soma == num:
  print(f"{num} é um numero perfeito!")
else:
  print(f"{num} não é um numero perfeito!")