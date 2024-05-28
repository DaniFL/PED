import sqlite3

def inicializar_base_datos():
    conexion = sqlite3.connect('noticias.db')
    cursor = conexion.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS noticias (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        autor TEXT NOT NULL,
                        titular TEXT NOT NULL,
                        contenido TEXT NOT NULL
                    )''')
    conexion.commit()
    conexion.close()

inicializar_base_datos()
