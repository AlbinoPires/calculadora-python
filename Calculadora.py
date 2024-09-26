#Exercicio de revisão

# Exercicio de revisão

while True:
    print("\n****  MENU  *************************\n")
    print("Hello, world!   Bem vindo à calculadora")
    print(f"\n- Digite 1 para realizar uma soma!")
    print(f"\n- Digite 2 para realizar uma subtração!")
    print(f"\n- Digite 3 para realizar uma divisão!")
    print(f"\n- Digite 4 para realizar uma multiplicação!")
    print(f"\n- Digite 5 para sair!")

    opcao = input("\nDigite a opção desejada: ")

    if opcao == '1':  # Comparar com string
        try:
            first_number = int(input("Digite o primeiro número positivo: "))
            second_number = int(input("Digite o segundo número positivo: "))

            if first_number < 0 or second_number < 0:
                raise ValueError("Digite números positivos!")
            result = first_number + second_number 
            print(f"\nO total de sua soma é {result}, obrigado!")
        except ValueError:
            print("\nERRO: Digite um número positivo!")

    elif opcao == '2':  # Comparar com string
        try:
            first_number = int(input("Digite o primeiro número positivo: "))
            second_number = int(input("Digite o segundo número: "))
            if first_number < 0 or second_number < 0:
                raise ValueError("Digite números positivos!")
            result = first_number - second_number
            print(f"\nO total de sua subtração é {result}")
        except ValueError:
            print("\nERRO: Digite um número positivo!")

    elif opcao == '3':  # Comparar com string
        try:
            first_number = int(input("Digite o primeiro número positivo: "))
            second_number = int(input("Digite o segundo número: "))
            if first_number < 0 or second_number < 0:
                raise ValueError("Digite números positivos!")
            if second_number != 0:
                result = first_number / second_number
                print(f"\nO total de sua divisão é {result}")
            else:
                print("\nERRO: Não é possível dividir por zero!")
        except ValueError:
            print("\nERRO: Digite um número positivo!")

    elif opcao == '4':  # Comparar com string
        try:
            first_number = int(input("Digite o primeiro número positivo: "))
            second_number = int(input("Digite o segundo número: "))
            if first_number < 0 or second_number < 0:
                raise ValueError("Digite números positivos!")
            result = first_number * second_number
            print(f"\nO total de sua multiplicação é {result}")
        except ValueError:
            print("\nERRO: Digite um número positivo!")

    elif opcao == '5':  # Comparar com string
        print("\nObrigado por utilizar minha calculadora!")
        break

    else:
        print("\nOpção inválida, tente novamente!")
