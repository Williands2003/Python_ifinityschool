produtos = {}

for i in range(5):
    nome = input(f"Digite o nome do produto {i + 1}: ")
    preco = float(input(f"Digite o preço do produto {nome}: "))
    produtos[nome] = preco

valor_total = sum(produtos.values())

print("Valor total da compra:", valor_total)
