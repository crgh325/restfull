from app import app

from app.models import Grupos
from app.models import Alumnos
# todo la libreria marshmallow me permite serializar
# todo los objetos de mi clase a un formato json
from flask_marshmallow import Marshmallow

ma = Marshmallow(app)


class GrupoSerializer(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Grupos
        fields = ('codgrupo', 'nombre_grupo', 'estado')


# todo lo utilizare cuando deseo mostrar solo un registro
grupo_schema = GrupoSerializer()
# todo lo utilizare cuando deseo mostrar varios
grupos_schema = GrupoSerializer(many=True)


class AlumnoSerializer(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Alumnos
        fields = ('cod_alum', 'nombre_alumno',
                  'apellido_alumno', "estado", "codgrupo")


# todo lo utilizare cuando deseo mostrar solo un registro
alumno_schema = AlumnoSerializer()
# todo lo utilizare cuando deseo mostrar varios
alumnos_schema = AlumnoSerializer(many=True)
