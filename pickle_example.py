import pickle
import csv
import os

def salvar_produtos(produtos):
    if os.path.exists('produtos.pickle'):
        limpar_arquivo()
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

def limpar_arquivo():
    with open('produtos.pickle', 'wb') as arquivo:
        arquivo.truncate(0)
    print("Arquivo limpo com sucesso!")

def eliminar_arquivo():
    if os.path.exists('produtos.pickle'):
        os.remove('produtos.pickle')
        print("Arquivo eliminado com sucesso!")
    else:
        print("Arquivo não encontrado.")

def exportar_para_csv(produtos):
    with open('produtos.csv', 'w', newline='') as arquivo_csv:
        escritor = csv.DictWriter(arquivo_csv, fieldnames=['nome', 'preco'])
        escritor.writeheader()
        for produto in produtos:
            escritor.writerow(produto)
    print("Produtos exportados para CSV com sucesso!")

def menu():
    print("\n### Menu ###")
    print("1. Adicionar Produto")
    print("2. Listar Produtos")
    print("3. Salvar Produtos")
    print("4. Carregar Produtos")
    print("5. Limpar Arquivo")
    print("6. Eliminar Arquivo")
    print("7. Exportar para CSV")
    print("8. Sair")

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
            limpar_arquivo()
        elif escolha == "6":
            eliminar_arquivo()
        elif escolha == "7":
            exportar_para_csv(produtos)
        elif escolha == "8":
            print("Saindo...")
            break
        else:
            print("Escolha inválida. Tente novamente.")
