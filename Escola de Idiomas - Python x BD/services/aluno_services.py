from config.db import criar_conexao

def cadastrar_aluno(nome_aluno: str, nascimento_aluno: str, cpf_aluno: int, email: str, senha: str):
    
    try:
        con = criar_conexao()
        cursor = con.cursor()

        sql_usuario = "INSERT INTO Usuario (email, senha) VALUES (%s, %s) RETURNING usuario_id;"
        cursor.execute(sql_usuario, (email, senha))
        usuario_id = cursor.fetchone()[0]

        sql = "INSERT INTO aluno(nome_aluno, nascimento_aluno, cpf_aluno, usuario_id) VALUES(%s, %s, %s, %s)"
        cursor.execute(sql, (nome_aluno, nascimento_aluno, cpf_aluno, usuario_id))
        con.commit()
        print("Aluno cadastrado com sucesso!")

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
