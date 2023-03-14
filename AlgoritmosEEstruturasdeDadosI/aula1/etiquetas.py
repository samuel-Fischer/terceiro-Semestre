# 8. Elaborar um programa que leia o nome de um produto e o número de etiquetas a serem impressas desse
# produto. Exiba as etiquetas com o nome do produto, com no máximo 2 etiquetas por linha, conforme
# exemplo de execução do programa, demonstrado a seguir.

etiqueta = input("Nome da etiqueta: ")
num = int(input("Numero de impressões: "))

for i in range(0,num//2,+1):
  print(etiqueta + "     " + etiqueta)

if num % 2 != 0:
  print(etiqueta)