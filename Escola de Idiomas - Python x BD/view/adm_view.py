from services.curso_services import cadastrar_curso, lista_curso, remover_curso, update_curso
from services.turma_services import cadastrar_turma, remover_turma, update_turma, adicionar_aluno, adicionar_professor
from services.aluno_services import remover_aluno, update_aluno
from services.professor_services import remover_professor, update_professor
from services.usuario_services import update_usuario_email_senha

def tabela(login_usuario):
    while True:
        print(f"Bem vindo(a): {login_usuario[1]}")
        if login_usuario:
            nivel = login_usuario[3]
            if nivel == 'admin':
                print(f"Bem vindo ADMIN: {login_usuario[1]}")
                print(" 1 - Registar\n 2 - Listar\n 3 - Atualizar\n 4 - Remover\n 5 - Deslogar")
                opcao = input("Digite a opção: ")
                match opcao:
                    case '1':
                        while True:
                            print(" 1 - Aluno\n 2 - Professor\n 3 - Turma\n 4 - Curso\n 5 - Voltar")
                            opcao_c_t = input("Digite a opção: ")
                            match opcao_c_t:
                                case '1':
                                    aluno_id = input("ID do aluno: ")
                                    turma_id = input("ID da turma: ")
                                    adicionar_aluno(aluno_id, turma_id)
                                case '2':
                                    professor_id = input("ID do professor: ")
                                    turma_id = input("ID da turma: ")
                                    adicionar_professor(professor_id, turma_id)
                                case '3':
                                    horario_turma = input("Horário: ")
                                    curso_id = input("ID do curso: ")
                                    cadastrar_turma(horario_turma, curso_id)
                                case '4':
                                    idioma_curso = input("Idioma: ")
                                    nome_curso = input("Nome do curso: ")
                                    horario_curso = input("Período do dia: ")
                                    cadastrar_curso(idioma_curso, nome_curso, horario_curso)
                                case '5':
                                    break
                                case _:
                                    print("Digite uma opção válida")
                    case '2':
                        cursos = lista_curso()
                        for curso in cursos:
                            print(curso)
                    case '3':
                        print(" 1 - Aluno\n 2 - Professor\n 3 - Turma\n 4 - Curso\n 5 - Voltar")
                        opcao_update = input("Digite a opção: ")
                        match opcao_update:
                            case '1':
                                usuario_id = input("Digite o ID para atualizar: ")
                                novo_email = input("Novo email: ")
                                nova_senha = input("Nova senha: ")
                                update_usuario_email_senha(usuario_id, novo_email, nova_senha)
                                id_update = input("Digite o ID para atualizar: ")
                                update_aluno(usuario_id, id_update)
                            case '2':
                                usuario_id = input("Digite o ID para atualizar: ")
                                novo_email = input("Novo email: ")
                                nova_senha = input("Nova senha: ")
                                update_usuario_email_senha(usuario_id, novo_email, nova_senha)
                                id_update = input("Digite o ID para atualizar: ")
                                update_professor(usuario_id, id_update)
                            case'3':
                                id_update = input("Digite o ID para atualizar: ")
                                novo_horario_turma = input("Digite o novo horário: ")
                                update_turma(id_update, novo_horario_turma)
                            case '4':
                                id_update = input("Digite o ID para atualizar: ")
                                novo_nome_curso = input("Digite o novo nome: ")
                                novo_horario_curso = input("Digite o novo turno: ")
                                update_curso(id_update, novo_nome_curso, novo_horario_curso)
                            case '5':
                                break
                            case _:
                                print("Digite uma opção válida")
                    case '4':
                        print(" 1 - Aluno\n 2 - Professor\n 3 - Turma\n 4 - Curso\n 5 - Voltar")
                        opcao_remover = input("Digite a opção: ")
                        match opcao_remover:
                            case '1':
                                id_remove = input("Digite o ID para remover: ")
                                remover_aluno(id_remove)
                            case '2':
                                id_remove = input("Digite o ID para remover: ")
                                remover_professor(id_remove)
                            case'3':
                                id_remove = input("Digite o ID para remover: ")
                                remover_turma(id_remove)
                            case '4':
                                id_remove = input("Digite o ID para remover: ")
                                remover_curso(id_remove)
                            case '5':
                                break
                            case _:
                                print("Digite uma opção válida")
                    case '5':
                        break
                    case _:
                        print("Digite uma opção válida")
            elif nivel == 'professor':
                    print(f"Bem vindo professor: {login_usuario[1]}")
                    print(" 1 - Registar\n 2 - Listar\n 3 - Atualizar\n 4 - Remover\n 5 - Deslogar")
                    opcao = input("Digite a opção: ")
                    match opcao:
                        case '1':
                            while True:
                                print(" 1 - Professor\n 3 - Voltar")
                                opcao_c_t = input("Digite a opção: ")
                                match opcao_c_t:
                                    case '1':
                                        professor_id = input("ID do professor: ")
                                        turma_id = input("ID da turma: ")
                                        adicionar_professor(professor_id, turma_id)
                                    case '2':
                                        break
                                    case _:
                                        print("Digite uma opção válida")
                        case '2':
                            cursos = lista_curso()
                            for curso in cursos:
                                print(curso)
                        case '3':
                            print(" 1 - Professor\n 2 - Voltar")
                            opcao_update = input("Digite a opção: ")
                            match opcao_update:
                                case '1':
                                    usuario_id = input("Digite o ID para atualizar: ")
                                    novo_email = input("Novo email: ")
                                    nova_senha = input("Nova senha: ")
                                    update_usuario_email_senha(usuario_id, novo_email, nova_senha)
                                    id_update = input("Digite o ID para atualizar: ")
                                    update_professor(usuario_id, id_update)
                                case '2':
                                    break
                                case _:
                                    print("Digite uma opção válida")
                        case '4':
                            print(" 1 - Professor\n 5 - Voltar")
                            opcao_remover = input("Digite a opção: ")
                            match opcao_remover:                           
                                case '1':
                                    id_remove = input("Digite o ID para remover: ")
                                    remover_professor(id_remove)
                                case '2':
                                    break
                                case _:
                                    print("Digite uma opção válida")
                        case '5':
                            break
                        case _:
                            print("Digite uma opção válida")
            elif nivel == 'aluno':
                print(f"Bem vindo aluno: {login_usuario[1]}")              
                print(" 1 - Registar\n 2 - Listar\n 3 - Atualizar\n 4 - Remover\n 5 - Deslogar")
                opcao = input("Digite a opção: ")
                match opcao:
                    case '1':
                        while True:
                            print(" 1 - Aluno\n 2 - Voltar")
                            opcao_c_t = input("Digite a opção: ")
                            match opcao_c_t:
                                case '1':
                                    aluno_id = input("ID do aluno: ")
                                    turma_id = input("ID da turma: ")
                                    adicionar_aluno(aluno_id, turma_id)
                                case '2':
                                    break
                                case _:
                                    print("Digite uma opção válida")
                    case '2':
                        cursos = lista_curso()
                        for curso in cursos:
                            print(curso)
                    case '3':
                        print(" 1 - Aluno\n 2 - Voltar")
                        opcao_update = input("Digite a opção: ")
                        match opcao_update:
                            case '1':
                                usuario_id = input("Digite o ID para atualizar: ")
                                novo_email = input("Novo email: ")
                                nova_senha = input("Nova senha: ")
                                update_usuario_email_senha(usuario_id, novo_email, nova_senha)
                                id_update = input("Digite o ID para atualizar: ")
                                update_aluno(usuario_id, id_update)
                            case '2':
                                break
                            case _:
                                print("Digite uma opção válida")
                    case '4':
                        print(" 1 - Aluno\n 2 - Voltar")
                        opcao_remover = input("Digite a opção: ")
                        match opcao_remover:
                            case '1':
                                id_remove = input("Digite o ID para remover: ")
                                remover_aluno(id_remove)
                            case '2':
                                break
                            case _:
                                print("Digite uma opção válida")
                    case '5':
                        break
                    case _:
                        print("Digite uma opção válida")