"""
El titulo de la serie con el promedio de edad de sus actores.

y el numero de premios que ha tenido esa serie
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import func

from modelo import Plataforma ,Premio,Serie,Actor
from configuracion import cadena_base_datos

engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

# titulos= ssession.query(Serie).join(Plataforma).((Actor)).all()
# act= session.query(Actor).join(Serie).all()

# promedio = session.query(func.avg(Actor.edad)).scalar().all()

# act= session.query(Actor).join(Serie).all()

prueba = session.query(Serie).all()
# resultados = db.session.query(
#     TuModelo.categoria, 
#     func.avg(TuModelo.precio)
# ).group_by(TuModelo.categoria).all()

print("Serie con la edad de sus actores")
print("============================================")
for t in prueba:
    print(f"Serie: {t.titulo} - Edad Actores: {t.promedio_edad_actores()} - Premios: {t.premios_serie()}")
    