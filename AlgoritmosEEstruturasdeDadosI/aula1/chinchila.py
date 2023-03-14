# 9. Digamos que o número de chinchilas de uma fazenda triplica a cada ano, após o primeiro ano. Elaborar um
# programa que leia o número inicial de chinchilas e anos e informe ano a ano o número médio previsto de
# chinchilas da fazenda. O número inicial de chinchilas deve ser maior ou igual a 2 (um casal). 

chinchilas = int(input("Numero de Chinchilas: "))
anos = int(input("Anos de criação: "))

if chinchilas < 2:
  print("Não é possivel iniciar uma criação de chincilas com apenas uma chinchila.")
else:
  for i in range(1,anos+1,+1):
    print(f"{i}º Ano: {chinchilas} chinchilas")
    chinchilas = chinchilas * 3