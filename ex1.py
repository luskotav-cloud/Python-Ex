def avaliar_forca_senha():
    nivelSenha = 0
    senha = str(input("Digite sua senha: "))
    caracteresEspeciais = "!@#$%&*"


    if len(senha) < 6:
        nivelSenha += 1
    elif len(senha) >= 6 and len(senha) <= 10 : 
        nivelSenha += 2
    else:
        nivelSenha += 3

    quantidadeEspeciais = sum(1 for c in senha if c in caracteresEspeciais)

    if quantidadeEspeciais >= 2:
        nivelSenha += 1  

    if nivelSenha >= 1 and nivelSenha < 2:
        print("Senha fraca")
    elif nivelSenha >= 2 and nivelSenha < 3 : 
        print("Senha média")
    else:
        print("Senha forte")
    print(len(senha))

avaliar_forca_senha()