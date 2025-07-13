import class_pokemon
import sqlite3

file = "./data_base/box_pokemon.db"
link = sqlite3.connect(file)
cursors = link.cursor()

def creation_table():
    cursors.execute('''
        CREATE TABLE IF NOT EXISTS Pokemon (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE NOT NULL,
            hp INT NOT NULL,
            attack INT NOT NULL
            defense INT NOT NULL,
            speed INT NOT NULL,
            type_ TEXT NOT NULL,
            attack1 INT NOT NULL,  
            attack2 INT NOT NULL,  
            attack3 INT NOT NULL,  
            attack4 INT NOT NULL,  
            precision FLOAT NOT NULL,
            esquive FLOAT NOT NULL
            img TEXT NOT NULL
        )
    ''') #We have to puts the attacks as integers, because we will use the id of the attack in the attack_set
    link.commit()


def create_pokemon(name, hp, attack, defense, speed, type_,  attack_set, precision, esquive, img):
    creation_table()

    try:
        cursors.execute('''
            INSERT INTO pokemon (name, hp, attack, defense, speed, type_,  attack_set, precision, esquive, img)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', (name, hp, attack, defense, speed, type_,  attack_set, precision, esquive, img))
        
        link.commit()
        print(f"✅ Pokémon '{name}' créé avec succès !")
    
    except sqlite3.IntegrityError:
        print(f"⚠️ Le nom de pokémon '{name}' existe déjà. Choisis-en un autre.")
    
    finally:
        link.close()


def edit_pokemon(name):
    creation_table()

    cursors.execute('''
        SELECT * FROM pokemon WHERE name = ?
    ''', (name))
    result = cursors.fetchone()
    if not result:
        print(f"⚠️ Aucun Pokémon trouvé avec le nom '{name}'.")
        return
    else:
        print(f"⚙️ Édition du Pokémon '{name}':")
    
    
    print(f"✅ Pokémon '{name}' mis à jour avec succès !")
    link.close()