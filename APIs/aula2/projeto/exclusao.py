import requests

itemId = int(input("Código do produto a ser deletado: "))

# URL da API para busca do produto
url = f'http://localhost:3000/produtos/{itemId}'

# Realize uma solicitação GET à API para obter o produto a ser deletado
response = requests.get(url)

# Obtenha o produto do JSON retornado pela API
produto = response.json()

# Realize uma solicitação DELETE à API para deletar o produto
response = requests.delete(url)

try:
  if response.status_code == 200:
    print(f'O pruduto {produto["descricao"]} foi deletado com sucesso!')
except:
    print('Erro ao deletar o produto.')