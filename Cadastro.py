usuarios = []

def cadastrar_usuario():
    nome = input("Digite seu nome: ")
    email = input("Digite seu e-mail: ")
    usuario = {"nome": nome, "email": email}
    usuarios.append(usuario)
    print("\nUsuário cadastrado com sucesso!\n")

def listar_usuarios():
    if not usuarios:
        print("\nNenhum usuário cadastrado ainda.\n")
    else:
        print("\nLista de usuários:")
        for i, usuario in enumerate(usuarios, 1):
            print(f"{i}. Nome: {usuario['nome']} | E-mail: {usuario['email']}")
        print()

while True:
    print("1. Cadastrar usuário")
    print("2. Listar usuários")
    print("3. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar_usuario()
    elif opcao == "2":
        listar_usuarios()
    elif opcao == "3":
        print("Saindo do sistema. Até logo!")
        break
    else:
        print("Opção inválida. Tente novamente.\n")
