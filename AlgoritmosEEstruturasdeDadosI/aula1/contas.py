# 6. Elaborar um programa que faça a leitura da descrição e valor de contas que devem ser pagas por um
# usuário, até ser digitado ‘Fim’ na descrição. As contas devem ser listadas ao final, com o número de contas
# (contador) e a soma dos valores (acumulador). Obs.: Ainda não usar listas (arrays).

contador = 0
total = 0
contas = ""

print("Programa Contas do Mês – Digite ‘Fim’ para sair")
print("-"*30)
while True:
  despesa = input("Qual depesa você deseja lançar: ")
  if despesa == "Fim":
    break
  valor = float(input("Valor da despesa: "))

  contador += 1
  total += total
  contas = contas + f"{despesa:.20s} {valor:6.2f}\n"

print("Contas do Mês")
print("-"*30)
print(contas)
print("-"*30)
print(f"{contador} conta(s) - Total R$ {total:.2f}")