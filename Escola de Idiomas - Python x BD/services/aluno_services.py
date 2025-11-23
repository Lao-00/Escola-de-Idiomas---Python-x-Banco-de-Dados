from config.db import criar_conexao

def cadastrar_aluno(nome_aluno: str, nascimento_aluno: str, cpf_aluno: int, email: str, senha: str):
    
    try:
        con = criar_conexao()
        cursor = con.cursor()

        sql_usuario = "INSERT INTO usuario (email, senha) VALUES (%s, %s) RETURNING usuario_id;"
        cursor.execute(sql_usuario, (email, senha))
        usuario_id = cursor.fetchone()[0]

        sql = "INSERT INTO aluno(nome_aluno, nascimento_aluno, cpf_aluno, usuario_id) VALUES(%s, %s, %s, %s) RETURNING aluno_id"
        cursor.execute(sql, (nome_aluno, nascimento_aluno, cpf_aluno, usuario_id))
        aluno_id, = cursor.fetchone()
        con.commit()
        print(f"ID do Aluno {aluno_id} cadastrado com sucesso!")

    except Exception as e:
        print(e)
    finally:
        cursor.close()
        con.close()

def login(email: str, senha: str):
    con = criar_conexao()
    cursor = con.cursor()
    sql = "SELECT * FROM usuario LEFT JOIN aluno ON usuario.usuario_id = aluno.usuario_id LEFT JOIN professor ON usuario.usuario_id = professor.usuario_id LEFT JOIN administrador ON usuario.usuario_id = administrador.usuario_id WHERE email = %s and senha = %s"
    cursor.execute(sql, (email, senha))
    usuario = cursor.fetchone()
    return usuario

def remover_aluno(aluno_id):

    try:
        con = criar_conexao()
        cursor = con.cursor()

        sql = 'DELETE FROM aluno WHERE aluno_id = %s'
        cursor.execute(sql, (aluno_id))
        con.commit()
        print("Aluno removido!")
        
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        con.close()

def update_aluno(aluno_id, usuario_id):

    try:
        con = criar_conexao()
        cursor = con.cursor()


        sql = 'UPDATE aluno SET usuario_id = %s WHERE aluno_id = %s'
        cursor.execute(sql, (usuario_id, aluno_id))
        con.commit()
        print("Dados do aluno atualizados!")
        
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        con.close()