import csv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from configuracion import cadena_base_datos
from modelo import Pais, Plataforma, Serie, Actor, Premio

engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

actores_csv = ["../data/actores.csv"]
for archivo_csv in actores_csv:
    with open(archivo_csv, "r", encoding="utf-8") as archivo:
        reader = csv.DictReader(archivo)
        for linea in reader:
            pais_obj = session.query(Pais).filter_by(nombre=linea["pais"]).first()
            serie_obj = session.query(Serie).filter_by(titulo=linea["serie"]).first()
            actor = Actor(
                id=int(linea["id"]),
                nombre=linea["nombre"],
                edad=int(linea["edad"]),
                pais=pais_obj,
                serie=serie_obj
            )
            session.add(actor)
    session.commit()
with open("../data/actores.csv", "r", encoding="utf-8") as archivo:
    reader = csv.DictReader(archivo)
    for linea in reader:
            pais_obj = session.query(Pais).filter_by(nombre=linea["pais"]).first()
            serie_obj = session.query(Serie).filter_by(titulo=linea["serie"]).first()
            actor = Actor(
                id=int(linea["id"]),
                nombre=linea["nombre"],
                edad=int(linea["edad"]),
                pais=pais_obj,
                serie=serie_obj
            )
            session.add(actor)
session.commit()