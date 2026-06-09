import csv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from configuracion import cadena_base_datos
from modelo import Pais, Plataforma, Serie, Actor, Premio

engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()


paises_csv = ["../data/paises.csv"]
for archivo_csv in paises_csv:
    with open(archivo_csv, "r", encoding="utf-8") as archivo:
        reader = csv.DictReader(archivo)
        for linea in reader:
            pais = Pais(
                id=int(linea["id"]),
                nombre=linea["nombre"],
                continente=linea["continente"]
            )
            session.add(pais)
    session.commit()
    