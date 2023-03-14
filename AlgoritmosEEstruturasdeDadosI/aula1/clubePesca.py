# 2. A entrada para um clube de pesca custa R$ 20,00 por pessoa e cada pessoa tem direito a levar um peixe.
# Peixes extras custam 12,00. Elabore um programa que leia o número de pessoas de uma família que foram ao
# clube e o número de peixes obtidos na pescaria. Informe o valor a pagar.

pessoas = int(input("Entrada para quantas pessoas? "))
peixes = int(input("Quantos peixes foram pescados? "))

valor = pessoas * 20
if peixes > pessoas:
  peixes_a_pagar = (peixes - pessoas) * 12
  valor += peixes_a_pagar

print(f"Você tera que pagar R$ {valor:.2f}.")