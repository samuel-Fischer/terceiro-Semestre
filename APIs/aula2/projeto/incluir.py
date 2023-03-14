import requests

# Lê as informações do novo produto do terminal
descricao = input("Digite o nome do produto: ")
marca = input("Digite a marca do produto: ")
quantidade = int(input("Digite a quantidade do produto: "))
preco = float(input("Digite o preço do produto: "))

# Monta o payload da requisição POST
payload = {
    'descricao': descricao,
    'marca': marca,
    'quant': quantidade,
    'preco': preco
}

# Envia a requisição POST para a API
response = requests.post('http://localhost:3000/produtos', json=payload)

# Verifica se a requisição foi bem-sucedida
if response.status_code == 201:
    print("Produto cadastrado com sucesso!")
else:
    print("Não foi possível cadastrar o produto.")
