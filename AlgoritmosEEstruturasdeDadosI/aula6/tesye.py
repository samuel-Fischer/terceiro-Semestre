nome_arq = input("Nome do Arquivo: ")
arq = open(nome_arq, "r")
# insere o texto e converte suas palavras em maisculas e adiciona as palavras a uma lista
palavras = []
for linha in arq:
    for palavra in linha.split():
        palavras.append(palavra.upper())

        # obtem o conjunto de palavras unicas e suas frequencias salvando essas associaçoes em um dicionario

        dicionario = {}
        for palavra in palavras:
            num = dicionario.get(palavra, None)
            # busca a palavra chave se nao exisitir: None
            num = dicionario.get(palavra, None)

            if num == None:
                # se nao existir, adicionar o valor 1
                dicionario[palavra] = 1
            else:
                # se existir, adciona mais 1
                dicionario[palavra] = num + 1
                # Encontra a mode(que mais aparece), obtem o valor
                # maximo no dicionario e  determina a sua chave
                maior = max(dicionario.values())
                for chave in dicionario:
                    if dicionario[chave] == maior:
                        print(f"A mode é: {chave}")

                        # obtem as 10 mais
                ordenadas = sorted(dicionario.items(),
                                   key=lambda d: d[1], reverse=True)

                for i, (palavra, quant) in enumerate(ordenadas, start=1):
                    print(f"{i}°: {palavra}- {quant}vezes")
                    if i == 20:
                        break
