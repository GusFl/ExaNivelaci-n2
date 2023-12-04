from app import db

class Carne(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    nombre = db.Column(db.String(255))
    descripcion = db.Column(db.String(255))
    precio = db.Column(db.String(255))
    preso = db.Column(db.String(255))

class Pan(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    tipo = db.Column(db.String(255))
    descripcion = db.Column(db.String(255))
    precio= db.Column(db.String(255))
    tamaño = db.Column(db.String(255))

class Carro(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    nombre = db.Column(db.String(255))
    kilometraje = db.Column(db.String(255))
    precio = db.Column(db.String(255))
    marca = db.Column(db.String(255))


class Computadora(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    nombre = db.Column(db.String(255))
    marca = db.Column(db.String(255))
    ram = db.Column(db.String(255))
    almacenamiento = db.Column(db.String(255))

class Bebida(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    nombre = db.Column(db.String(255))
    marca = db.Column(db.String(255))
    precio = db.Column(db.String(255))
    color = db.Column(db.String(255))