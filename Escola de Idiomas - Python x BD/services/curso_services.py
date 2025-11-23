from config.db import criar_conexao

def cadastrar_curso(idioma_curso: str, nome_curso: str, horario_curso: str):

    try:
        con = criar_conexao()
        cursor = con.cursor()

        sql = "INSERT INTO curso(idioma_curso, nome_curso, horario_curso) VALUES(%s, %s, %s) RETURNING curso_id"
        cursor.execute(sql, (idioma_curso, nome_curso, horario_curso))
        curso_id, = cursor.fetchone()
        con.commit()
        print(f"ID do Curso {curso_id} cadastrado com sucesso!")

    except Exception as e:
        print(e)
    finally:
        cursor.close()
        con.close()

def lista_curso():

    try:
        con = criar_conexao()
        cursor = con.cursor()

        sql = 'SELECT * FROM curso LEFT JOIN turma ON turma.curso_id = curso.curso_id'
        cursor.execute(sql)
        lista = cursor.fetchall()

        return lista
    
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        con.close()

def remover_curso(curso_id):

    try:
        con = criar_conexao()
        cursor = con.cursor()

        sql = 'DELETE FROM curso WHERE curso_id = %s'
        cursor.execute(sql, (curso_id))
        con.commit()
        print("Curso removido!")
        
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        con.close()

def update_curso(nome_curso, horario_curso, curso_id):

    try:
        con = criar_conexao()
        cursor = con.cursor()


        sql = 'UPDATE curso SET nome_curso = %s, horario_curso = %s WHERE curso_id = %s'
        cursor.execute(sql, (nome_curso, horario_curso, curso_id))
        con.commit()
        print("Dados do curso atualizados!")
        
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        con.close()