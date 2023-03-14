# 3. Uma farmácia necessita de um programa que leia o total de uma compra. Exiba como resposta o nº
# máximo de vezes que o cliente pode parcelar essa compra e o valor de cada parcela. Considere as seguintes
# condições: a) cada parcela deve ser de, no mínimo, R$ 20,00; b) o número máximo de parcelas permitido é 6.

valorTotal = int(input("Valor a pagar: "))

for i in range(6, 1, -1):
  if valorTotal / i >= 20:
    valorAPagar = valorTotal / i
    print(f"Você pode pagar em até {i}X de R$ {valorAPagar:,.2f}.".format(valorTotal))
    break
  elif valorTotal < 40:
    print(f"Você pode pagar em 1X de R$ {valorTotal:,.2f}.".format(valorTotal))
    break