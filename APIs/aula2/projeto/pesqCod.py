import requests
import locale

# Lê as informações do novo produto do terminal
itemId = int(input("Código do produto: "))
# Realize uma solicitação GET à API
response = requests.get(f'http://localhost:3000/produtos/{itemId}')
# Defina a localidade para o Brasil
locale.setlocale(locale.LC_ALL, 'pt_BR.utf-8')
# Obtenha a lista de produtos do JSON retornado pela API
produto = response.json()

try:
    # Obtenha a lista de produtos do JSON retornado pela API
    produto = response.json()

    # Imprima os detalhes dos produtos em uma tabela formatada
    print('{:^5} | {:<20} | {:<20} | {:^12} | {:^10}'.format(' ID', 'Nome', 'Marca', 'Quantidade', 'Preço'))
    print('-' * 80)

    # Formate o preço para reais
    preco_formatado = locale.currency(produto['preco'], grouping=True, symbol=None)
    print('{:^5} | {:<20} | {:<20} | {:^12} | R${:>9}'.format(produto['id'], produto['descricao'], produto['marca'], produto['quant'], preco_formatado))
except:
    print('\n{0:^80}'.format("Nenhum código foi encontrado!"))