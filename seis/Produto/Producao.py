from Produto import Produto
from Venda import Venda

def menu():
    print("( ͡~ ͜ʖ ͡°)")
    print("1. ADICIONAR PRODUTO")
    print("2. REMOVER PRODUTO")
    print("3. LISTAR PRODUTOS")
    print("4. MOSTRAR TOTAL")
    print("5. SAIR")

def main():
    venda = Venda("01/09/2024")
    
    while True:
        menu()
        escolha = input("ESCOLHA UMA OPÇÃO: ")
        
        if escolha == "1":
            nome = input("DIGITE O NOME DO PRODUTO: ")
            preco = float(input("DIGITE O PREÇO DO PRODUTO: "))
            quantidade = int(input("DIGITE A QUANTIDADE DO PRODUTO: "))
            produto = Produto(nome, preco, quantidade)
            venda.adicionar_produto(produto)
            print(f"PRODUTO {nome} ADICIONADO COM SUCESSO.")
        
        elif escolha == "2":
            nome = input("DIGITE O NOME DO PRODUTO A SER REMOVIDO: ")
            if venda.remover_produto(nome):
                print(f"PRODUTO {nome} REMOVIDO COM SUCESSO.")
            else:
                print(f"PRODUTO {nome} NÃO ENCONTRADO.")
        
        elif escolha == "3":
            produtos = venda.listar_produtos()
            if produtos:
                print("PRODUTOS NA VENDA:")
                for p in produtos:
                    print(f"NOME: {p[0]}, PREÇO: {p[1]}, QUANTIDADE: {p[2]}")
            else:
                print("NENHUM PRODUTO NA VENDA.")
        
        elif escolha == "4":
            total = venda.calcularTotal()
            print(f"TOTAL DA VENDA: R$ {total:.2f}")
        
        elif escolha == "5":
            print("SAINDO... ٩(▀̿Ĺ̯▀̿ ̿٩)三")
            break
        
        else:
            print("OPÇÃO INVÁLIDA, TENTE NOVAMENTE.")

if __name__ == "__main__":
    main()