import csv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from configuracion import cadena_base_datos
from modelo import Pais, Plataforma, Serie, Actor, Premio

engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

with open("../data/premios.csv", "r", encoding="utf-8") as archivo:
    reader = csv.DictReader(archivo)
    for linea in reader:
        serie_obj = session.query(Serie).filter_by(titulo=linea["serie"]).first()
        premio = Premio(
            id=int(linea["id"]),
            nombre_premio=linea["nombre_premio"],
            categoria=linea["categoria"],
            anio=int(linea["anio"]),
            serie=serie_obj
        )
        session.add(premio)
session.commit()

