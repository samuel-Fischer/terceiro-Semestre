# 1. Que leia descrição e preco de ‘n’ produtos, até o usuário digitar ‘Fim’ na descrição. Ao final, exiba:
# - A quantidade de itens informados
# - O total dos itens
# - O preço e produto de maior valor
# - O valor médio dos produtos
from statistics import fmean

produtos = []
valores = []

print("\nInforme 'Fim' para sair.")
while True:
  x = input("\nNome do produto: ")
  if x == "Fim":
    break
  y = float(input("Valor do produto: "))
  produtos.append(x)
  valores.append(y)


if len(valores) == 0:
    print("Nenhum produto informado.")
else:
    index = valores.index(max(valores))
    produtoCaro = produtos[index]

print(f"Quantidade: {len(produtos)}")
print(f"Valor médio: {fmean(valores):.2f}")
print(f"Valor total: {sum(valores):.2f}")
print(f"O produto: {produtoCaro} custa: {max(valores):.2f}")