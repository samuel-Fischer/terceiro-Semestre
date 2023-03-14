# 10. Elaborar um programa que leia a altura de uma árvore (número de linhas) e após exiba a árvore iniciando
# com 2 estrelas (asteriscos) e aumentando em 2 a cada linha. Fazer com que a árvore tenha uma margem
# esquerda fixa de 30 espaços e fique centralizada, conforme ilustra a execução do programa a seguir: 

altura = int(input("Qual o tamanho da árvore: "))
espaco = " "

if altura % 2 != 0:
  altura += 1

for i in range(1,altura+1,1):
  linha = "**"
  altura -= 1
  print(f"{espaco*29}{espaco*altura}{linha*i}")