# 3. Que receba um valor e uma taxa de desconto. A taxa de desconto deve ter o valor padrão de 10%.
# Calcule e exiba o valor com desconto.

def calcula_desconto(valor, desconto=10):
  valor_desconto = valor * (desconto / 100)
  novo_valor = valor - valor_desconto
  print(f"Valor com Desconto: {novo_valor}")