from flask import Blueprint, request,jsonify
from models import Carro
from app import db

appcarro= Blueprint('appcarro',__name__,template_folder="templates")

@appcarro.route('/carro/agregar',methods={'POST'})
def agregaCarro():
    try:
        json = request.get_json()
        carro = Carro()
        carro.nombre = json['nombre']
        carro.kilometraje = json['kilometraje']
        carro.precio = json['precio']
        carro.marca = json['marca']
        db.session.add(carro)
        db.session.commit()
        return jsonify({"status":200, "mensaje":"carro agregado"})
    except Exception as ex:
        return jsonify({"status":400,"mensaje":ex})

@appcarro.route('/carro/editar',methods={"POST"})
def editaCarro():
    try:
        json = request.get_json()
        carro = Carro.query.get_or_404(json['id'])
        carro.nombre = json['nombre']
        carro.kilometraje = json['kilometraje']
        carro.precio = json['precio']
        carro.marca = json['marca']
        db.session.commit()
        return jsonify({'status':"OK",'mensaje':"carro modificado"})
    except Exception as ex:
        return jsonify({"status":"ERROR","mensaje":ex})
    
@appcarro.route('/carro/eliminar',methods={"POST"})
def eliminaCarro():
    try:
        json = request.get_json()
        carro = Carro.query.get_or_404(json['id'])
        db.session.delete(carro)
        db.session.commit()
        return jsonify({'status':"OK",'mensaje':"carro eliminado"})
    except Exception as ex:
        return jsonify({"status":"ERROR","mensaje":ex})

@appcarro.route('/carro/obtener',methods={"GET"})
def obtenerCarro():
    carros = Carro.query.all()
    listaCarros=[]
    for r in carros:
        carro = {}
        carro['nombre'] = r.nombre
        carro['kilometraje'] = r.kilometraje
        carro['precio'] = r.precio
        carro['marca'] = r.marca
        listaCarros.append(carro)
    return jsonify({'carro':listaCarros})