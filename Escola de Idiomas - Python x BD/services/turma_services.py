from config.db import criar_conexao

def cadastrar_turma(horario_turma):

    try:
        con = criar_conexao()
        cursor = con.cursor()

        sql = "INSERT INTO turma(horario_curso) VALUES(%s)"
        cursor.execute(sql, (horario_turma))
        con.commit()
        print("Turma cadastrada com sucesso!")

    except Exception as e:
        print(e)
    finally:
        cursor.close()
        con.close()