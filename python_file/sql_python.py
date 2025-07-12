import sqlite3

fichier = "./data_base/box.db"
link = sqlite3.connect(fichier)
cursors = link.cursor()

def creation_table():
    cursors.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    ''')
    link.commit()
    print("✅ Table 'users' créée ou déjà existante.")

def register_user(username, password):
    creation_table()
    try:
        cursors.execute('''
            INSERT INTO users (username, password)
            VALUES (?, ?)''', (username, password))
        
        link.commit()
        print(f"✅ Utilisateur '{username}' créé avec succès !")
    
    except sqlite3.IntegrityError:
        print(f"⚠️ Le nom d'utilisateur '{username}' existe déjà. Choisis-en un autre.")
    
    finally:
        link.close()  











def __main__():
    username = input("Choisis un nom d'utilisateur : ")
    password = input("Choisis un mot de passe : ")
    register_user(username, password)


__main__()