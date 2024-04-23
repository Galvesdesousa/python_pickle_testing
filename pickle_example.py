import pickle

def salvar_produtos(produtos):
    with open('produtos.pickle', 'wb') as arquivo:
        pickle.dump(produtos, arquivo)
    print("Produtos salvos com sucesso!")

def carregar_produtos():
    try:
        with open('produtos.pickle', 'rb') as arquivo:
            produtos = pickle.load(arquivo)
        print("Produtos carregados com sucesso!")
        return produtos
    except FileNotFoundError:
        print("Arquivo de produtos não encontrado. Criando nova lista.")
        return []

def adicionar_produto(produtos):
    nome = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço do produto: "))
    produtos.append({"nome": nome, "preco": preco})
    print("Produto adicionado com sucesso!")

def listar_produtos(produtos):
    if produtos:
        print("Lista de produtos:")
        for produto in produtos:
            print(f"Nome: {produto['nome']}, Preço: {produto['preco']}")
    else:
        print("Nenhum produto na lista.")

def menu():
    print("\n### Menu ###")
    print("1. Adicionar Produto")
    print("2. Listar Produtos")
    print("3. Salvar Produtos")
    print("4. Carregar Produtos")
    print("5. Sair")

    escolha = input("Escolha uma opção: ")
    return escolha

if __name__ == "__main__":
    produtos = []
    while True:
        escolha = menu()
        if escolha == "1":
            adicionar_produto(produtos)
        elif escolha == "2":
            listar_produtos(produtos)
        elif escolha == "3":
            salvar_produtos(produtos)
        elif escolha == "4":
            produtos = carregar_produtos()
        elif escolha == "5":
            print("Saindo...")
            break
        else:
            print("Escolha inválida. Tente novamente.")