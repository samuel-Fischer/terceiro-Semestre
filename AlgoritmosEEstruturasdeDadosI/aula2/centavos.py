# 4. Que receba o preço de um produto e retorne apenas os centavos do preço.

import math

def centavos(preco):
  preco_sem_centavos = math.floor(preco)
  return preco - preco_sem_centavos