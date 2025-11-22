from config.db import criar_conexao

def update_usuario_email_senha(novo_email, nova_senha, usuario_id):

    try:
        con = criar_conexao()
        cursor = con.cursor()


        sql = 'UPDATE usuario SET email = %s, senha = %s WHERE usuario_id = %s'
        cursor.execute(sql, (novo_email, nova_senha, usuario_id))
        con.commit()
        print("Dados do usuário atualizados!")
        
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        con.close()