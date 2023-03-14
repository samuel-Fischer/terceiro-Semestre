# 4. Elaborar um programa que leia um número – que deve ser uma centena (como um valor inteiro). Calcule e
# exiba a centena invertida. Caso o número não seja uma centena, exiba mensagem.

numero = input("Centena: ")
if len(numero) != 3:
  print("O numero não é uma centena!")
else:
  numero = numero[::-1]
  print(f"{numero}")