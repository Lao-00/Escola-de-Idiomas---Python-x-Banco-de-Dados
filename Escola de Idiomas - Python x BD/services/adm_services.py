from config.db import criar_conexao

def cadastrar_adm(nome_adm: str, email: str, senha: str):
    
    try:
        con = criar_conexao()
        cursor = con.cursor()

        sql_usuario = "INSERT INTO usuario (email, senha) VALUES (%s, %s) RETURNING usuario_id;"
        cursor.execute(sql_usuario, (email, senha))
        usuario_id = cursor.fetchone()[0]

        sql = "INSERT INTO administrador(nome_adm, usuario_id) VALUES(%s, %s)"
        cursor.execute(sql, (nome_adm, usuario_id))
        con.commit()
        print("Adm cadastrado com sucesso!")

    except Exception as e:
        print(e)
    finally:
        cursor.close()
        con.close()


