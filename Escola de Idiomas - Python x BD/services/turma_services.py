from config.db import criar_conexao
#from services.curso_services import cadastrar_curso

def cadastrar_turma(horario_turma: str, curso_id: int):
    
    try:
        con = criar_conexao()
        cursor = con.cursor()

        sql = "INSERT INTO turma(horario_turma, curso_id) VALUES(%s, %s) RETURNING turma_id"
        cursor.execute(sql, (horario_turma, curso_id))
        turma_id = cursor.fetchone()
        con.commit()
        print("Turma cadastrada com sucesso!")


    except Exception as e:
        print(e)
    finally:
        cursor.close()
        con.close()

def remover_turma(turma_id):

    try:
        con = criar_conexao()
        cursor = con.cursor()

        sql = 'DELETE FROM turma WHERE turma_id = %s'
        cursor.execute(sql, (turma_id))
        con.commit()
        print("Turma removida!")
        
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        con.close()

def update_turma(horario_turma, turma_id):

    try:
        con = criar_conexao()
        cursor = con.cursor()


        sql = 'UPDATE turma SET horario_turma = %s WHERE turma_id = %s'
        cursor.execute(sql, (horario_turma, turma_id))
        con.commit()
        print("Dados da turma atualizados!")
        
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        con.close()

def adicionar_aluno(aluno_id, turma_id):

    try:
        con = criar_conexao()
        cursor = con.cursor()

        sql = 'UPDATE turma SET aluno_id = %s WHERE turma_id = %s'
        cursor.execute(sql, (aluno_id, turma_id))
        con.commit()
        print("Aluno matriculado na turma com sucesso!")

    except Exception as e:
        print(e)
    finally:
        cursor.close()
        con.close()

def adicionar_professor(professor_id, turma_id,):

    try:
        con = criar_conexao()
        cursor = con.cursor()

        sql = 'UPDATE turma SET professor_id = %s WHERE turma_id = %s'
        cursor.execute(sql, (professor_id, turma_id))
        con.commit()
        print("Professor registrado com sucesso!")

    except Exception as e:
        print(e)
    finally:
        cursor.close()
        con.close()