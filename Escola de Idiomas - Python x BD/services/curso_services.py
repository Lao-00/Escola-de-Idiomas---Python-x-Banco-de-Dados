from config.db import criar_conexao

def cadastrar_curso(idioma_curso: str, nome_curso: str, horario_curso: str):

    try:
        con = criar_conexao()
        cursor = con.cursor()

        sql = "INSERT INTO curso(idiomas_curso, nome_curso, horario_curso) VALUES(%s, %s, %s, %s)"
        cursor.execute(sql, (idioma_curso, nome_curso, horario_curso))
        con.commit()
        print("Curso cadastrado com sucesso!")

    except Exception as e:
        print(e)
    finally:
        cursor.close()
        con.close()