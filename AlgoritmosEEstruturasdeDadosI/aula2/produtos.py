# 1. Que leia descrição e preco de ‘n’ produtos, até o usuário digitar ‘Fim’ na descrição. Ao final, exiba:
# - A quantidade de itens informados
# - O total dos itens
# - O preço e produto de maior valor
# - O valor médio dos produtos

# biblioteca para funções de calculos
from statistics import fmean

produtos = []
precos = []

print("Informe os produtos e FIM para sair.")
while True:
    x = input("Produtos: ")
    if x == "FIM":
        break
    y = float(input("Preços R$: "))
    produtos.append(x)
    precos.append(y)

    print()
    print("-"*30)
    quant = len(produtos)
    soma = sum(precos)
    media = fmean(precos)
    maior = max(precos)
    
    try:
        indice_maior = precos.index(maior)
        produto_maior = produtos[indice_maior]
    except ValueError:
        print("Error...")

print(f"Quantidade de Produtos {quant}")
print(f"Soma dos Preços R$ {soma:6.2f}")
print(f"Média dos Preços R$: {media:6.2f}")
print(f"Mario Valor R$: {maior:6.2f} - {produto_maior}")
      