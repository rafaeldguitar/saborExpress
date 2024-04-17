import os

restaurantes = [{"nome":"Praça", "categoria":"Japonesa", "ativo":False}, #metodo de dicionario
                {"nome":"Pizza Suprema", "categoria":"Pizza", "ativo":True},
                {"nome":"Cantina", "categoria":"Italiano", "ativo":False}]

def voltar_ao_menu_principal():
    input("\nClique enter para voltar ao menu pricipal.")
    main()

def exibir_subtitulos(texto):
    os.system("cls")
    linha = "*" * (len(texto)) # pega o numero de caracteres de texto
    print(linha)
    print(texto)
    print(linha)
    print()

def exibir_opcoes():
    print("1 - Cadastrar restaurante")
    print("2 - Listar restaurante")
    print("3 - Alternar estado do restaurante")
    print("4 - Sair")

def exibir_nome_do_programa():
    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
      """)

def cadastrar_novo_restaurante():
    exibir_subtitulos("Cadastro de novos restaurantes")
    nome_do_restaurante = input("Digite o nome do restaurante: ")
    categoria = input("Digite a categoria do restaurante: ")
    dados_do_restaurante = {"nome":nome_do_restaurante, "categoria":categoria, "ativo":False}  
    #restaurantes.append(nome_do_restaurante) #adciona na lista
    restaurantes.append(dados_do_restaurante)
    print(f"\nO restaurante {nome_do_restaurante} foi adicionado na lista!")
    voltar_ao_menu_principal()
    
def listar_restaurantes():
    exibir_subtitulos("Lista de restaurantes cadastrados")

    print(f"{"| Nome do restaurante".ljust(22)} | {"Categoria".ljust(20)} | Status")
    for restaurante in restaurantes: #para cada restaurante na lista restaurantes
        nome_restaurante = restaurante["nome"]
        categoria_restaurante = restaurante["categoria"]
        ativo = "Ativado" if restaurante["ativo"] else "Desativado"
        print(f"| {nome_restaurante.ljust(20)} | {categoria_restaurante.ljust(20)} | {ativo}") #.ljust cria um espaçamento padrao

    voltar_ao_menu_principal()

def alternar_estado_restaurante():
    exibir_subtitulos("Alternando estado do restaurante")
    nome_restaurante = input("\nDigite o nome do restaurante: ")
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante["nome"]:
            restaurante_encontrado = True
            restaurante["ativo"] = not restaurante["ativo"] #inverte true false
            mensagem = f"\nO restaurante foi ativado com sucesso!" if restaurante["ativo"] else f"\nO restaurante {nome_restaurante} fo desativado com sucesso!"
            print(mensagem)

    if not restaurante_encontrado:
        print("O restaurante não foi encontrado.")

    voltar_ao_menu_principal()

def esclher_opcao():
    try: #tente...
        opcao_escolhida = int(input("\nEscolha uma opção: ")) #variavel em python separar com _ | int para o format poder ler
        #print("Você escolheu a opção ", opcao_escolhida)
        #print("Você escolheu a opção {}".format(opcao_escolhida))
        #print(f"Você escolheu a opção {opcao_escolhida}") #melhor escolha
        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternar_estado_restaurante()
        elif opcao_escolhida == 4:
            finalizando_app()
        else:
            opcao_invalida()
    except: #se o try nao der certo
        opcao_invalida()

def finalizando_app(): #função
    exibir_subtitulos("Encerrando...")

def opcao_invalida():
    print("Opção invalida!\n")
    voltar_ao_menu_principal()

def main():
    os.system("cls")
    exibir_nome_do_programa()
    exibir_opcoes()
    esclher_opcao()

if __name__ == "__main__": #transforma esse arquivo no main
    main()