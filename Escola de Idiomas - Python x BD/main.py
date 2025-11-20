from services.aluno_services import cadastrar_aluno, login
from services.professor_services import cadastrar_professor
from services.adm_services import cadastrar_adm
from services.curso_services import cadastrar_curso
from services.turma_services import cadastrar_turma
import getpass
import os

def clear_screen():
    # Check the operating system
    if os.name == 'nt':  # For Windows
        _ = os.system('cls')
    else:  # For macOS and Linux
        _ = os.system('clear')


while True:
    print(" 1 - Cadastrar\n 2 - Login\n 3 - Sair")
    opcao = int(input("Digite a opção: "))
    clear_screen()

    if opcao == 1:
        print(" 1 - Aluno\n 2 - Professor")
        opcao_cadastro = int(input("Digite a opção: "))
        clear_screen()

        if opcao_cadastro == 1:
            nome_aluno = input("Nome: ")
            nascimento_aluno = input("Data de nascimento: ")
            cpf_aluno = int(input("CPF: "))
            email = input("E-Mail: ")
            senha = input("Senha: ")
            cadastrar_aluno(nome_aluno, nascimento_aluno, cpf_aluno, email, senha)
            #clear_screen()
        elif opcao_cadastro == 2:
            nome_professor = input("Nome: ")
            especialidade_professor = input("Especialidade: ")
            cpf_professor = int(input("CPF: "))
            email = input("E-Mail: ")
            senha = input("Senha: ")
            cadastrar_professor(nome_professor, especialidade_professor, cpf_professor, email, senha)
            #clear_screen()
    elif opcao == 2:
        email = input("E-Mail: ")
        senha = getpass.getpass("Senha: ")
        login_usuario = login(email, senha)
        #clear_screen()
        if login_usuario:
            print(login_usuario)
        else:
            print("Usuário ou senha inválidos")
    elif opcao == 3:
        break
    else:
        print("Digite uma opção válida")