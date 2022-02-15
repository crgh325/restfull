class Config(object):
    # todo conectado a la base de datos de MYSQL
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:cargamos2022@localhost/bdcargamos'
    SQLALCHEMY_TRACK_MODIFICATIONS = True


"""
# pip install psycopg2-binary
class Config(object):
    # todo conectado a la base de datos de MYSQL
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:cargamos2022@localhost/bdcargamos'

    #SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:rioazulq12@localhost:5432/bdcargamos'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
"""
