import csv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from configuracion import cadena_base_datos
from modelo import Pais, Plataforma, Serie, Actor, Premio

engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

with open("../data/series.csv", "r", encoding="utf-8") as archivo:
    reader = csv.DictReader(archivo)
    for linea in reader:
        pais_obj = session.query(Pais).filter_by(nombre=linea["pais"]).first()
        plataforma_obj = session.query(Plataforma).filter_by(nombre=linea["plataforma"]).first()
        serie = Serie(
            id=int(linea["id"]),
            titulo=linea["titulo"],
            genero=linea["genero"],
            anio_estreno=int(linea["anio_estreno"]),
            temporadas=int(linea["temporadas"]),
            pais=pais_obj,
            plataforma=plataforma_obj
        )
        session.add(serie)
session.commit()
