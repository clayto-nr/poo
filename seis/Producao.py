from Autor import Autor
from Livro import Livro
from Biblioteca import Biblioteca

def menu():
    print("\n" + "="*30)
    print("(✌ﾟ∀ﾟ)☞ MENU PRINCIPAL ( ˘▽˘)っ♨")
    print("="*30)
    print("1. Adicionar livro")
    print("2. Remover livro")
    print("3. Buscar livro")
    print("4. Listar todos os livros")
    print("5. Sair")
    print("="*30)

def obter_inteiro(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Valor inválido. Por favor, insira um número inteiro.")

def main():
    biblioteca = Biblioteca()
    
    while True:
        menu()
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            print("\n" + "-"*30)
            print("Adicionar Novo Livro")
            print("-"*30)
            nome_autor = input("Nome do autor: ")
            nacionalidade_autor = input("Nacionalidade do autor: ")
            dataNascimento_autor = input("Data de nascimento do autor: ")
            autor = Autor(nome_autor, nacionalidade_autor, dataNascimento_autor)

            titulo_livro = input("Título do livro: ")
            anoPublicacao_livro = obter_inteiro("Ano de publicação do livro: ")
            livro = Livro(titulo_livro, autor, anoPublicacao_livro)

            biblioteca.adicionarLivro(livro)
            print("\nLivro adicionado com sucesso!")

        elif opcao == '2':
            print("\n" + "-"*30)
            print("Remover Livro")
            print("-"*30)
            titulo_livro = input("Título do livro a ser removido: ")
            biblioteca.removerLivro(titulo_livro)
            print("\nLivro removido com sucesso!")

        elif opcao == '3':
            print("\n" + "-"*30)
            print("Buscar Livro")
            print("-"*30)
            titulo_livro = input("Título do livro a ser buscado: ")
            resultado = biblioteca.buscarLivro(titulo_livro)
            print("\nResultado da busca:")
            print(resultado)

        elif opcao == '4':
            print("\n" + "-"*30)
            print("Lista de Livros")
            print("-"*30)
            livros = biblioteca.listarLivros()
            if livros:
                for livro in livros:
                    print(livro)
            else:
                print("\nNenhum livro disponível na biblioteca.")

        elif opcao == '5':
            print("\n" + "="*30)
            print("Saindo... Até logo iefi, eri, eno!")
            print("="*30)
            break

        else:
            print("\nOpção inválida. Tente novamente.")

if __name__ == "__main__":
    main()