import requests
import locale

# Realize uma solicitação GET à API
response = requests.get('http://localhost:3000/produtos')
# Defina a localidade para o Brasil
locale.setlocale(locale.LC_ALL, 'pt_BR.utf-8')

# Obtenha a lista de produtos do JSON retornado pela API
produtos = response.json()

# Imprima os detalhes dos produtos em uma tabela formatada
print('{:^5} | {:<20} | {:<20} | {:^12} | {:^10}'.format(' ID', 'Nome', 'Marca', 'Quantidade', 'Preço'))
print('-' * 80)
for produto in produtos:
    # Formate o preço para reais
    preco_formatado = locale.currency(produto['preco'], grouping=True, symbol=None)
    print('{:^5} | {:<20} | {:<20} | {:^12} | R${:>9}'.format(produto['id'], produto['descricao'], produto['marca'], produto['quant'], preco_formatado))

if len(produtos) == 0:
  print('\n{0:^80}'.format("Sua loja está vazia!"))