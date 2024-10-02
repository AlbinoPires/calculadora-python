#Sistema de gerenciamento de estudante
class Estudante:

    def __init__(self, nome, idade, nota1):
        self.nome = nome
        self.idade = idade
        self.nota1 = nota1

    def get_nome(self):
        return self.nome
    
    def set_nome(self, nome):
        self.nome = nome

    def get_idade(self):
        return self.idade
    
    def set_idade(self, idade):
        self.idade = idade

    def get_nota1(self):
        return self.nota1
    
    def set_nota1(self, nota1):
        self.nota1 = nota1

def menu():

    estudantes = []

    while True:

        print("1. Adicionar um novo estudante")
        print("2. Atualizar a nota do estudante existente")
        print("3. Visualizar informações de um estudante")
        print("4. Listar todos os estudantes")
        print("5. Sair")

        escolha = input("\nEscolha uma opção\n")

        if escolha == "1":

            nome = input("\nDigite o nome do estudante: \n")

            idade = int(input("\Digite a idade do estudante: \n"))

            nota1 = float(input("\Digite a nota do estudante: \n"))

            novo_estudante = Estudante(nome, idade, nota1)

            estudantes.append(novo_estudante)

            print(f"Estudante {nome} adicionado com sucesso!")

        elif escolha == "2":

            nome = input("\nDigite o nome do estudante para atualizar a nota: ")  # Corrigido para input()

            for estudante in estudantes:

                if estudante.get_nome() == nome:

                    nova_nota1 = float(input("\nDigite a nova nota: \n"))

                    estudante.set_nota1(nova_nota1)

                    print("\nNota atualizada com sucesso")

                    break

            else:
                print("\nEstudante não encontrado.")

        elif escolha == "3":

            nome = input("\nDigite o nome do estudante para visualizar as informações: ")

            for estudante in estudantes:
                if estudante.get_nome() == nome:
                    print(f"\nEstudante {estudante.get_nome()}, Idade: {estudante.get_idade()}, Nota: {estudante.get_nota1()}")

                    break

            else:

                print("\nEstudante não encontrado!")

        elif escolha == "4":

            print("\nListando todos os estudantes:")

            for estudante in estudantes:
                print(f"\nEstudante {estudante.get_nome()}, Idade: {estudante.get_idade()}, Nota: {estudante.get_nota1()}\n")

        elif escolha == "5":
            print("\nObrigado!")
            break

        else:
            print("Opção Invalida!")

#verifica se este script e o ponto de entrada para execução
if __name__ == "__main__":

    menu()







    
