from flask import Blueprint, request,jsonify
from models import Bebida
from app import db

appbebida= Blueprint('appbebida',__name__,template_folder="templates")

@appbebida.route('/bebida/agregar',methods={'POST'})
def agregaBebida():
    try:
        json = request.get_json()
        bebida = Bebida()
        bebida.nombre = json['nombre']
        bebida.marca = json['marca']
        bebida.precio = json['precio']
        bebida.color = json['color']
        db.session.add(bebida)
        db.session.commit()
        return jsonify({"status":200, "mensaje":"bebida agregado"})
    except Exception as ex:
        return jsonify({"status":400,"mensaje":ex})

@appbebida.route('/bebida/editar',methods={"POST"})
def editaBebida():
    try:
        json = request.get_json()
        bebida = Bebida.query.get_or_404(json['id'])
        bebida.nombre = json['nombre']
        bebida.marca = json['marca']
        bebida.precio = json['precio']
        bebida.color = json['color']
        db.session.commit()
        return jsonify({'status':"OK",'mensaje':"bebida modificado"})
    except Exception as ex:
        return jsonify({"status":"ERROR","mensaje":ex})
    
@appbebida.route('/bebida/eliminar',methods={"POST"})
def eliminaBebida():
    try:
        json = request.get_json()
        bebida = Bebida.query.get_or_404(json['id'])
        db.session.delete(bebida)
        db.session.commit()
        return jsonify({'status':"OK",'mensaje':"bebida eliminado"})
    except Exception as ex:
        return jsonify({"status":"ERROR","mensaje":ex})

@appbebida.route('/bebida/obtener',methods={"GET"})
def obtenerBebida():
    bebidas = Bebida.query.all()
    listaBebidas=[]
    for r in bebidas:
        bebida = {}
        bebida['nombre'] = r.nombre
        bebida['marca'] = r.marca
        bebida['precio'] = r.precio
        bebida['color'] = r.color
        listaBebidas.append(bebida)
    return jsonify({'bebida':listaBebidas})