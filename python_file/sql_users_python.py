import sqlite3

file = "./data_base/box.db"
link = sqlite3.connect(file)
cursors = link.cursor()

def creation_table():
    cursors.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            role TEXT NOT NULL
        )
    ''')
    link.commit()
    #print("✅ Table 'users' créée ou déjà existante.")


def handle_user(action):
    username = input("Choisis un nom d'utilisateur : ")
    password = input("Choisis un mot de passe : ")

    if action == "login":
        connect_user(username, password)
    elif action == "register":
        register_user(username, password)
    else:
        print("⚠️ Action non reconnue. Choisissez 'login' ou 'register'.")


def register_user(username, password):
    creation_table()
    try:
        cursors.execute('''
            INSERT INTO users (username, password, role)
            VALUES (?, ?, ?)''', (username, password, "player"))
        
        link.commit()
        print(f"✅ Utilisateur '{username}' créé avec succès !")
    
    except sqlite3.IntegrityError:
        print(f"⚠️ Le nom d'utilisateur '{username}' existe déjà. Choisis-en un autre.")
    
    finally:
        link.close()  


def connect_user(username, password):
    creation_table()
    cursors.execute('''
        SELECT * FROM users WHERE username = ? AND password = ?
    ''', (username, password))
    
    user = cursors.fetchone()
    
    if user:
        print(f"✅ Connexion réussie pour l'utilisateur '{username}' !")
    else:
        print("⚠️ Nom d'utilisateur ou mot de passe incorrect.")
    
    link.close()









def __main__():
    handle_user(action=input("Choisissez une action (login/register): ").strip().lower())
__main__()