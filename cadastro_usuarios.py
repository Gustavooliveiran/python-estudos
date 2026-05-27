usuarios = []

while True:
    print("\n1 - Cadastrar usuário")
    print("2 - Listar usuários")
    print("3 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Digite o nome: ")
        idade = input("Digite a idade: ")

        usuario = {
            "nome": nome,
            "idade": idade
        }

        usuarios.append(usuario)

        print("Usuário cadastrado com sucesso!")

    elif opcao == "2":
        print("\nLista de usuários:")

        for usuario in usuarios:
            print(f"Nome: {usuario['nome']} | Idade: {usuario['idade']}")

    elif opcao == "3":
        print("Programa encerrado.")
        break

    else:
        print("Opção inválida.")
