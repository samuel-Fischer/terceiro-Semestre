import requests

# Lê as informações do novo produto do terminal
itemId = int(input("Código do produto a ser alterado: "))
url = f'http://localhost:3000/produtos/{itemId}'
response = requests.get(url)
produto = response.json()

print(f'Nome atual do produto: {produto["descricao"]}')
descricao = input("Digite o nome do produto: ")
print(f"Marca atual do produto: {produto['marca']}")
marca = input("Digite a marca do produto: ")
print(f"Quantidade atual do produto: {produto['quant']}")
quantidade = int(input("Digite a quantidade do produto: "))
print(f"Preço atual do produto: {produto['preco']}")
preco = float(input("Digite o preço do produto: "))

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
