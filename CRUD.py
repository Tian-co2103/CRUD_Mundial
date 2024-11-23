from pymongo import MongoClient


client = MongoClient('mongodb://localhost:27017/')

db = client.copa_mundial

equipos_collection = db.equipos


def crear_equipos():
    equipos = [
        {
            "nombre": "Brasil",
            "estadio": "Maracanã",
            "ciudad_origen": "Río de Janeiro",
            "entrenador": "Tite",
            "jugadores_disponibles": 23
        },
        {
            "nombre": "Argentina",
            "estadio": "La Bombonera",
            "ciudad_origen": "Buenos Aires",
            "entrenador": "Lionel Scaloni",
            "jugadores_disponibles": 23
        },
        {
            "nombre": "Francia",
            "estadio": "Parque de los Príncipes",
            "ciudad_origen": "París",
            "entrenador": "Didier Deschamps",
            "jugadores_disponibles": 23
        },
        {
            "nombre": "Alemania",
            "estadio": "Allianz Arena",
            "ciudad_origen": "Múnich",
            "entrenador": "Hansi Flick",
            "jugadores_disponibles": 23
        },
        {
            "nombre": "España",
            "estadio": "Santiago Bernabéu",
            "ciudad_origen": "Madrid",
            "entrenador": "Luis de la Fuente",
            "jugadores_disponibles": 23
        },
        {
            "nombre": "Italia",
            "estadio": "San Siro",
            "ciudad_origen": "Milán",
            "entrenador": "Roberto Mancini",
            "jugadores_disponibles": 23
        },
        {
            "nombre": "Inglaterra",
            "estadio": "Wembley",
            "ciudad_origen": "Londres",
            "entrenador": "Gareth Southgate",
            "jugadores_disponibles": 23
        },
        {
            "nombre": "Países Bajos",
            "estadio": "Johan Cruyff Arena",
            "ciudad_origen": "Ámsterdam",
            "entrenador": "Ronald Koeman",
            "jugadores_disponibles": 23
        }
    ]
    
    equipos_collection.insert_many(equipos)
    print("Equipos insertados exitosamente.")


def obtener_equipos():
    equipos = equipos_collection.find()
    for equipo in equipos:
        print(equipo)


def actualizar_jugadores(nombre_equipo, nuevos_jugadores):
    equipos_collection.update_one(
        {"nombre": nombre_equipo},
        {"$set": {"jugadores_disponibles": nuevos_jugadores}}
    )
    print(f"Jugadores actualizados para el equipo {nombre_equipo}.")


def eliminar_equipo(nombre_equipo):
    equipos_collection.delete_one({"nombre": nombre_equipo})
    print(f"Equipo {nombre_equipo} eliminado.")

# Ejemplo operacion CRUD
if __name__ == "__main__":
    
    crear_equipos()
    
    
    print("Equipos actuales:")
    obtener_equipos()
    
    actualizar_jugadores("Brasil", 22)
    
   
    print("\nEquipos después de actualización:")
    obtener_equipos()
    
   
    eliminar_equipo("Italia")
    
    
    print("\nEquipos después de eliminar Italia:")
    obtener_equipos()