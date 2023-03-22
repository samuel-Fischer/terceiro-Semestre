import requests
import locale

locale.setlocale(locale.LC_ALL, 'pt_BR.utf-8')
url_api = "http://localhost:3000/produtos/"

def titulo(texto, sublinhado="-"):
  print()
  print(texto)
  print(sublinhado*40)

def incluir():
  try:
    descricao = input("\nDigite o nome do produto: ")
    marca = input("Digite a marca do produto: ")
    quantidade = int(input("Digite a quantidade do produto: "))
    preco = float(input("Digite o preço do produto: "))

    payload = {
      'descricao': descricao,
      'marca': marca,
      'quant': quantidade,
      'preco': preco
    }

    response = requests.post(url_api, json=payload)

    print("\nProduto cadastrado com sucesso!")
  except:
    print("\nNão foi possível cadastrar o produto.")

def listar():
  response = requests.get(url_api)
  produtos = response.json()

  print('\n{:^5} | {:<20} | {:<20} | {:^12} | {:^10}'.format(
    ' ID',
    'Nome',
    'Marca',
    'Quantidade',
    'Preço')
    )
  print('-' * 80)

  for produto in produtos:
    preco_formatado = locale.currency(produto['preco'], grouping=True, symbol=None)
    print('{:^5} | {:<20} | {:<20} | {:^12} | R${:>9}'.format(
      produto['id'],
      produto['descricao'],
      produto['marca'],
      produto['quant'],
      preco_formatado))

  if len(produtos) == 0:
    print('\n{0:^80}'.format("Sua loja está vazia!"))
    
def alterar():
  try:  
    itemId = int(input("\nCódigo do produto a ser alterado: "))
    url = f'{url_api}{itemId}'
    response = requests.get(url)
    produto = response.json()

    print(f'\nNome atual do produto: {produto["descricao"]}')
    descricao = input("Digite o nome do produto: ")
    print(f"\nMarca atual do produto: {produto['marca']}")
    marca = input("Digite a marca do produto: ")
    print(f"\nQuantidade atual do produto: {produto['quant']}")
    quantidade = int(input("Digite a quantidade do produto: "))
    print(f"\nPreço atual do produto: {produto['preco']}")
    preco = float(input("Digite o preço do produto: "))

    novo_produto = {
      'descricao': descricao,
      'marca': marca,
      'quant': quantidade,
      'preco': preco
    }

    response = requests.put(url, json=novo_produto)

    print(f'\nProduto atualizado com sucesso!')
  except:
    print('\nErro ao atualizar o produto:')

def excluir():
  try:
    itemId = int(input("\nCódigo do produto a ser deletado: "))
    url = f'{url_api}{itemId}'

    response = requests.get(url)
    produto = response.json()
    response = requests.delete(url)

    print(f'\nO pruduto {produto["descricao"]} foi deletado com sucesso!')
  except:
    print('\nErro ao deletar o produto.')

def pesquisar():
  try:
    itemId = int(input("\nCódigo do produto: "))
    url = f'{url_api}{itemId}'
    response = requests.get(url)
    produto = response.json()

    print('\n{:^5} | {:<20} | {:<20} | {:^12} | {:^10}'.format(
      ' ID',
      'Nome',
      'Marca',
      'Quantidade',
      'Preço')
      )
    print('-' * 80)

    locale.setlocale(locale.LC_ALL, 'pt_BR.utf-8')
    preco_formatado = locale.currency(produto['preco'], grouping=True, symbol=None)
    print('{:^5} | {:<20} | {:<20} | {:^12} | R${:>9}'.format(
      produto['id'],
      produto['descricao'],
      produto['marca'],
      produto['quant'],
      preco_formatado)
      )
  except:
    print('\n{0:^80}'.format("Nenhum código foi encontrado!"))

def estatisticas():
  response = requests.get(url_api)
  produtos = response.json()
  valor_total = 0
  produto_estoque = 0
  # criando um conjunto das marcas únicas
  fornecedores = set(produto['marca'] for produto in produtos)
  

  for produto in produtos:
    valor_total = valor_total + (produto['preco'] * produto['quant'])
    produto_estoque = produto_estoque + produto['quant']

  valorTotal_formatado = locale.currency(valor_total, grouping=True, symbol=None)
  print(f"\nValor total em produtos: {valorTotal_formatado}")
  print(f"Total de produtos em estoque: {produto_estoque}")
  print(f"Total de produtos cadastrados: {len(produtos)}")
  print(f"Total de marccas/fornecedores: {len(fornecedores)}")

while True:
  titulo('\n{:^40}'.format("Cadastro de produtos - consumo API", "="))
  print("1. Incluir de Produtos")
  print("2. Listagem de Produtos")
  print("3. Alteração de Produtos")
  print("4. Exclusão de Produtos")
  print("5. Pesquisa de Produtos")
  print("6. Dados Estatisticos")
  print("7. Finalizar")

  opcao = int(input("\nEscolha uma opção: "))
  if opcao == 1:
    incluir()
  elif opcao == 2:
    listar()
  elif opcao == 3:
    alterar()
  elif opcao == 4:
    excluir()
  elif opcao == 5:
    pesquisar()
  elif opcao == 6:
    estatisticas()
  elif opcao == 7:
    break