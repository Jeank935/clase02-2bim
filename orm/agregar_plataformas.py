import csv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from configuracion import cadena_base_datos
from modelo import Pais, Plataforma, Serie, Actor, Premio

engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()


with open("../data/plataformas.csv", "r", encoding="utf-8") as archivo:
    reader = csv.DictReader(archivo)
    for linea in reader:
        pais_obj = session.query(Pais).filter_by(nombre=linea["pais"]).first()
        plataforma = Plataforma(
            id=int(linea["id"]),
            nombre=linea["nombre"],
            suscriptores_millones=float(linea["suscriptores_millones"]),
            pais=pais_obj
        )
        session.add(plataforma)
session.commit()