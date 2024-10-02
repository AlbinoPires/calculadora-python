# Projeto I - Sistema de Gerenciamento de Livraria

## Descrição

Este projeto é um sistema simples de gerenciamento de uma livraria, criado em Python utilizando Programação Orientada a Objetos (POO). O sistema permite a interação dos usuários com os livros disponíveis, possibilitando o cadastro de usuários, consulta ao acervo, solicitação de empréstimos e devolução de livros.

## Funcionalidades Implementadas

1. **Classes**:
    - **Livro**: Representa os livros com atributos como título, autor, ano de publicação e disponibilidade.
    - **Usuário**: Representa os usuários da livraria, com atributos como nome e ID do usuário.
    - **Biblioteca**: Gerencia os livros e usuários, permitindo adicionar livros, registrar usuários, emprestar e devolver livros.

2. **Funcionalidades**:
    - Adicionar novos livros à biblioteca.
    - Registrar novos usuários.
    - Permitir que usuários solicitem empréstimos e devolvam livros.
    - Listar todos os livros disponíveis e emprestados.
    - Pesquisar livros por título ou autor.

## Progresso e Recursos

O sistema foi desenvolvido com uma interface simples e interativa, onde os usuários podem facilmente navegar pelas opções disponíveis. Até o momento, as funcionalidades básicas foram implementadas e testadas, garantindo uma usabilidade sem transtornos. No entanto, a persistência de dados não foi implementada nesta versão.

## Próximas Atualizações

Na atualização **1.1**, planejamos implementar a persistência de dados utilizando um banco de dados, permitindo que as informações sobre livros e usuários sejam salvas e acessadas mesmo após o fechamento do programa.

## Contribuições

Estamos abertos a sugestões e melhorias! Se você deseja contribuir para este projeto, fique à vontade para abrir uma issue ou enviar um pull request.

## Licença

Este projeto é de código aberto. Sinta-se à vontade para utilizá-lo e modificá-lo conforme necessário.







*************************************************************************************************************************
# Sistema de Gerenciamento de Estudantes
************************************************************************************************************************

Este repositório contém dois projetos em Python: uma calculadora simples e um sistema de gerenciamento de estudantes.

## Sist_gerenc_estudante.py

O arquivo `Sist_gerenc_estudante.py` é um sistema para gerenciar informações de estudantes, incluindo:

- Adicionar novos estudantes com nome, idade e nota.
- Atualizar a nota de um estudante existente.
- Visualizar informações de um estudante específico.
- Listar todos os estudantes registrados.

### Funcionalidades

- **Adicionar Estudante**: Permite que o usuário insira o nome, idade e nota do estudante.
- **Atualizar Nota**: O usuário pode atualizar a nota de um estudante já cadastrado.
- **Visualizar Estudante**: É possível buscar e visualizar as informações de um estudante específico.
- **Listar Estudantes**: Lista todos os estudantes cadastrados.

### Como usar

1. Execute o script em um ambiente Python.
2. Siga as instruções exibidas no menu para interagir com o sistema.

**Nota:** Certifique-se de ter Python instalado e que o arquivo esteja configurado corretamente para execução.

### Observação:

- **Dados Persistentes - esse código não inside em interação com nenhuma biblioteca ou banco de dados, trarei a implementação
com dados persistentes, com sqlite3 ou BD MySQL.







******************************************************************************************************************************************************
Codigo da  Calculadora em Python
*******************************************************************************************************************************************************
(Atualizando RADME.MD incluindo informacoes sobre sistema de gerenciamento de estudantes em POO)
Este projeto é uma calculadora simples desenvolvida em Python. O objetivo é revisar operações matemáticas básicas
e implementar boas práticas de código. Fiz uma implementação em que somente é permitido uso de numeros inteiros. 
A calculadora suporta as seguintes operações:

- Soma
- Subtração
- Multiplicação
- Divisão

## Como Usar

1. Clone o repositório para o seu ambiente local:
    ```bash
    git clone https://github.com/AlbinoPires/calculadora-python.git
    ```

2. Navegue até o diretório do projeto:
    ```bash
    cd calculadora-python
    ```

3. Execute o script principal da calculadora:
    ```bash
    python calculadora.py
    ```

4. Siga as instruções no menu da calculadora para realizar operações matemáticas.

## Funcionalidades

- **Soma**: Permite somar dois números inteiros.
- **Subtração**: Permite subtrair dois números inteiros.
- **Multiplicação**: Multiplica dois números inteiros.
- **Divisão**: Realiza a divisão entre dois números inteiros.
- Validação de entradas: Se o usuário digitar um valor inválido, uma mensagem de erro é exibida.

## Exemplo de Uso
**** MENU ****

Bem vindo à calculadora

Digite 1 para realizar uma soma!
Digite 2 para realizar uma subtração!
Digite 3 para realizar uma divisão!
Digite 4 para realizar uma multiplicação!
Digite 5 para sair!
Digite a opção desejada: 1 Digite o primeiro número positivo: 10 Digite o segundo número positivo: 20 O total de sua soma é 30, obrigado!
