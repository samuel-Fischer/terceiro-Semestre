# 1. Elaborar um programa que leia a distância percorrida por um ciclista em metros. 
# Exiba o equivalente em km e metros.

distanciaPercorrida = int(input("Digite a distância percorrida em metros: "))
distanciaKm = distanciaPercorrida // 1000 # o "//" retorna a o numero inteiro da divisão 
distanciaMt = int(distanciaPercorrida % 1000)

print(f"A distância percorrida é de {distanciaKm}km e {distanciaMt} metros.")