# Demonstraremos montagem de um projeto de livraria para teste de conhecimento

class Livro:
    def __init__(self, livro, autor, ano_publicacao, disponibilidade):
        self.livro = livro
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.disponibilidade = disponibilidade

    def verificar_disponibilidade(self):
        return "Disponível" if self.disponibilidade else "Indisponível"

    def __str__(self):
        return f"{self.livro} - {self.autor} ({self.ano_publicacao})"

# Criando a lista de livros
lista_de_livros = [
    Livro("1984", "Autor: George Orwell", 1949, True),
    Livro("Dom Casmurro", "Machado de Assis", 1899, True),
    Livro("O Senhor dos Anéis: A Sociedade do Anel", "J.R.R. Tolkien", 1954, False),
    Livro("Orgulho e Preconceito", "Jane Austen", 1813, True),
    Livro("O Pequeno Príncipe", "Antoine de Saint-Exupéry", 1943, False),
    Livro("A Revolução dos Bichos", "George Orwell", 1945, True),
    Livro("Cem Anos de Solidão", "Gabriel García Márquez", 1967, True),
    Livro("Moby Dick", "Herman Melville", 1851, True),
    Livro("O Alquimista", "Paulo Coelho", 1988, False),
    Livro("A Metamorfose", "Franz Kafka", 1915, True)
]

def menu():
    while True:
        print("\nBem vindo a Livraria, escolha uma opção:")
        print("1. Cadastrar usuário")
        print("2. Consulta ao nosso acervo")
        print("3. Devolução de livro")
        print("4. Solicitar empréstimo de exemplar")
        print("5. Doar um livro")
        print("6. Sair")

        escolha = input("\nDigite o número da sua escolha: ")

        if escolha == "1":
            nome = input("Digite seu nome: ")
            
            while True:
                telefone = input("Digite seu telefone com os 9 dígitos (SEM DDD): ")
                
                if len(telefone) != 9 or not telefone.isdigit():
                    print("\nDIGITE SEU TELEFONE CORRETAMENTE!\n")
                else:
                    print(f"\n Olá {nome}, seus foram cadastrados com sucesso!\n")
                    break  # Sai do loop se o telefone for válido


        elif escolha == "2":
            print("\nAcervo disponível:")
            for i, livro in enumerate(lista_de_livros, start=1):  # Enumerando a lista para mostrar índices
                print(f"{i}. {livro}")  # Isso chamará o método __str__ de cada objeto Livro

        elif escolha == "3":

            for i, livro in enumerate(lista_de_livros, start=1):  # Enumerando a lista para mostrar índices
                print(f"{i}. {livro}")  # Isso chamará o método __str__ de cada objeto Livro
            devolucao = input("\nDigite o numero do exemplar que deseja devolver: ")

            print("\nObrigado, enviaremos um SMS com as recomendações da devolução!\n")
            

        elif escolha == "4":
            print("\nAcervo disponível para empréstimo:")
            for i, livro in enumerate(lista_de_livros, start=1):
                status = "Disponível" if livro.disponibilidade else "Indisponível"
                print(f"{i}. {livro} - {status}")  # Mostra o livro e sua disponibilidade

            numero_livro = int(input("Digite o número do exemplar disponível na lista: ")) - 1  # Subtrai 1 para ajustar o índice

            if 0 <= numero_livro < len(lista_de_livros):
                livro_escolhido = lista_de_livros[numero_livro]
                if livro_escolhido.disponibilidade:
                    print(f"O exemplar de \"{livro_escolhido.livro}\" pode ser retirado na loja física mais próxima. Obrigado!")
                    livro_escolhido.disponibilidade = False  # Atualiza a disponibilidade para indisponível
                else:
                    print(f"O exemplar de \"{livro_escolhido.livro}\" não está disponível no momento.")
            else:
                print("Número de livro inválido.")



        elif escolha == "5":
            
            livro_doado = input("\nDigite o nome do exemplar a ser doado: ")
            autor_l_d = input("\nDigite o nome do autor: \n")
            ano_lancamento = input("\nDigite o ano do lançamento do exemplar: \n")

            print(f"\nO exemplar: {livro_doado}, do autor {autor_l_d}, lançado em {ano_lancamento}, foi cadastrado com sucesso!\n", 
                         "Você receberá um SMS para o telefone cadastrado com as instruções para prosseguirmos!")
            

        elif escolha == "6":
            print("ainda por fazer")
            break

        else:
            print("Escolha inválida, tente novamente!")

if __name__ == "__main__":
    menu()
