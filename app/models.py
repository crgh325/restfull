from app import db


class Grupos(db.Model):
    codgrupo = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre_grupo = db.Column(db.String(50))
    estado = db.Column(db.Integer)

    # todo crear constructor cuando se desea pasar valores al servicio
    def __init__(self, nombre_grupo, estado):
        self.nombre_grupo = nombre_grupo
        self.estado = estado


class Alumnos(db.Model):
    codalum = db.Colun(db.Integer, primary_key=True, autoincrement=True)
    nombre_alumno = db.Column(db.String(50))
    apellido_alumno = db.Column(db.String(50))
    estado = db.Column(db.Integer)
    codgrupo = db.Column(db.String(10))

    def __init__(self, nombre_alumno, apellido_alumno, estado, codgrupo):
        self.nombre_alumno = nombre_alumno
        self.apellido_alumno = apellido_alumno
        self.estado = estado
        codgrupo = codgrupo
