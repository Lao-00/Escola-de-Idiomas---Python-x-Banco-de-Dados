from config.db import criar_conexao

def cadastrar_professor(nome_professor: str, especialidade_professor: str, cpf_professor: int, email: str, senha: str):
    
    try:
        con = criar_conexao()
        cursor = con.cursor()

        sql_usuario = "INSERT INTO usuario (email, senha, tipo_usuario) VALUES (%s, %s, %s) RETURNING usuario_id;"
        cursor.execute(sql_usuario, (email, senha, 'professor'))
        usuario_id = cursor.fetchone()[0]

        sql = "INSERT INTO professor(nome_professor, especialidade_professor, cpf_professor, usuario_id) VALUES(%s, %s, %s, %s) RETURNING professor_id"
        cursor.execute(sql, (nome_professor, especialidade_professor, cpf_professor, usuario_id))
        professor_id, = cursor.fetchone()
        con.commit()
        print(f"ID do Professor {professor_id} cadastrado com sucesso!")

    except Exception as e:
        print(e)
    finally:
        cursor.close()
        con.close()

def remover_professor(professor_id):

    try:
        con = criar_conexao()
        cursor = con.cursor()

        sql = 'DELETE FROM professor WHERE professor_id = %s'
        cursor.execute(sql, (professor_id))
        con.commit()
        print("Professor removido!")
        
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        con.close()

def update_professor(usuario_id, professor_id):

    try:
        con = criar_conexao()
        cursor = con.cursor()


        sql = 'UPDATE professor SET usuario_id = %s WHERE professor_id = %s'
        cursor.execute(sql, (usuario_id, professor_id))
        con.commit()
        print("Dados do professor atualizados!")
        
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        con.close()