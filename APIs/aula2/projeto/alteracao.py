import requests

# Lê as informações do novo produto do terminal
itemId = int(input("Código do produto a ser alterado: "))
descricao = input("Digite o nome do produto: ")
marca = input("Digite a marca do produto: ")
quantidade = int(input("Digite a quantidade do produto: "))
preco = float(input("Digite o preço do produto: "))

# URL da API para atualização do produto
url = f'http://localhost:3000/produtos/{itemId}'

# Novos dados do produto
novo_produto = {
  'descricao': descricao,
  'marca': marca,
  'quant': quantidade,
  'preco': preco
}

# Realize uma solicitação PUT à API
response = requests.put(url, json=novo_produto)

# Verifique se a solicitação foi bem-sucedida
if response.status_code == 200:
  print('Produto atualizado com sucesso!')
else:
  print('Erro ao atualizar o produto:', response.text)
