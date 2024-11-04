import os

# Dicionário 
restaurantes = [{'nome': 'Dominus', 'categoria': 'Pizzaria', 'ativo':False},
                {'nome': 'Made in Japan', 'categoria': 'Japonesa', 'ativo':True},
                {'nome': 'Big Burguer', 'categoria': 'Hamburgueria', 'ativo':False}]
 
def exibir_nome_do_programa():
    print('TASTE EXPRESS')
    
    # Menu principal
def exibir_opcoes():
    print('1. Cadastrar resturante')
    print('2. Listar restaurante')
    print('3. Alternar estado do restaurante')
    print('4. Sair')

# Função para finalizar o app 
def finalizar_app():
    exibir_subtitulo('Encerrando\n')

# Função que retorna 
def voltar_ao_menu():
    input('\nAperte ENTER para voltar ao menu principal ') 
    main();


def exibir_subtitulo(texto): 
    os.system('cls')
    print(texto)
    print()

# função para quando uma ação for invalida e retornar ao menu principal
def opcao_invalida(): 
        print('Opção inválida!\n')
        voltar_ao_menu()

# função para cadastrar restaurante
def cadastrar_restaurante(): 
    exibir_subtitulo('Cadastrar restaurante')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite a categoria do restaurante {nome_do_restaurante}: ')
    dados_do_restaurante = {'nome': nome_do_restaurante, 'categoria':categoria, 'ativo':False}
    restaurantes.append(dados_do_restaurante)
    os.system('cls')
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')
    voltar_ao_menu()

# Função para mostrar lista de restaurantes e incrementar as opções na lista
def listar_restaurantes(): 
    exibir_subtitulo('Listando restaurantes')
    print(f'{'NOME DO RESTAURANTE'.ljust(22)} | {'CATEGORIA'.ljust(20)} | STATUS')

# Incrementa no dicionário 
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'Aberto' if restaurante['ativo'] else 'Fechado'
        print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}') 

    voltar_ao_menu()

def ativar_restaurante():
    exibir_subtitulo('Alternando estado do restaurante') 
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar: ') 
    resturante_encontrado = False  
    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            resturante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            if restaurante['ativo']:
                mensagem = f'O restaurante {nome_restaurante} foi aberto!'
            else:
                mensagem = f'O restaurante {nome_restaurante} foi fechado!'
            print(mensagem) 

    if not restaurante:
        print('o restaurante não foi encontrado')

    voltar_ao_menu()


 # Função para acessar as opções do menu principal
def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))

        if opcao_escolhida == 1: 
            cadastrar_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            ativar_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else: 
            opcao_invalida() 
    except:
         opcao_invalida()

# Função para retornar as funções do menu principal
def main(): 
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__': 
    main()
