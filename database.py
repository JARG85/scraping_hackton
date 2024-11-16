import psycopg2

def create_table(conn, table_name):
    """Crea una tabla en una base de datos PostgreSQL.

    Args:
        conn: Una conexión a la base de datos.
        table_name: El nombre de la tabla a crear.
    """

    sql = """
    CREATE TABLE IF NOT EXISTS {} (
        razon_social VARCHAR(255) NOT NULL,
        nit VARCHAR(20) PRIMARY KEY,
        categoria VARCHAR(100),
        servicio TEXT
    )
    """.format(table_name)
    
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    cur.close()

# Ejemplo de uso:
conn = psycopg2.connect(
    database="mydatabase",
    user="myuser",
    password="mypassword",
    host="localhost",
    port="5432"
)

create_table(conn, "empresas")

conn.close()