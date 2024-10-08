def criar_produto(nome, codigo, preco, estoque):
    return (nome, codigo, preco, estoque)

def atualizar_estoque(produto, quantidade):
    return (produto[0], produto[1], produto[2], produto[3] + quantidade)

def listar_produtos(produtos):
    for produto in produtos:
        print(f'Nome: {produto[0]}, Código: {produto[1]}, Preço: {produto[2]}, Estoque: {produto[3]}')

produtos = []
produtos.append(criar_produto("Arroz", 101, 5.50, 10))
produtos.append(criar_produto("Feijão", 102, 7.25, 8))
produtos.append(criar_produto("Macarrão", 103, 3.20, 15))

listar_produtos(produtos)

produtos[0] = atualizar_estoque(produtos[0], 5)
print("\nApós atualizar o estoque do arroz:")
listar_produtos(produtos)
