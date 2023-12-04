from flask import Blueprint, request,jsonify
from models import Computadora
from app import db

appcomputadora= Blueprint('appcomputadora',__name__,template_folder="templates")

@appcomputadora.route('/computadora/agregar',methods={'POST'})
def agregaComputadora():
    try:
        json = request.get_json()
        computadora = Computadora()
        computadora.nombre = json['nombre']
        computadora.marca = json['marca']
        computadora.ram = json['ram']
        computadora.almacenamiento = json['almacenamiento']
        db.session.add(computadora)
        db.session.commit()
        return jsonify({"status":200, "mensaje":"computadora agregado"})
    except Exception as ex:
        return jsonify({"status":400,"mensaje":ex})

@appcomputadora.route('/computadora/editar',methods={"POST"})
def editaComputadora():
    try:
        json = request.get_json()
        computadora = Computadora.query.get_or_404(json['id'])
        computadora.nombre = json['nombre']
        computadora.marca = json['marca']
        computadora.ram = json['ram']
        computadora.almacenamiento = json['almacenamiento']
        db.session.commit()
        return jsonify({'status':"OK",'mensaje':"computadora modificado"})
    except Exception as ex:
        return jsonify({"status":"ERROR","mensaje":ex})
    
@appcomputadora.route('/computadora/eliminar',methods={"POST"})
def eliminaComputadora():
    try:
        json = request.get_json()
        computadora = Computadora.query.get_or_404(json['id'])
        db.session.delete(computadora)
        db.session.commit()
        return jsonify({'status':"OK",'mensaje':"computadora eliminado"})
    except Exception as ex:
        return jsonify({"status":"ERROR","mensaje":ex})

@appcomputadora.route('/computadora/obtener',methods={"GET"})
def obtenerComputadora():
    computadoras = Computadora.query.all()
    listaComputadoras=[]
    for r in computadoras:
        computadora = {}
        computadora['nombre'] = r.nombre
        computadora['marca'] = r.marca
        computadora['ram'] = r.ram
        computadora['almacenamiento'] = r.almacenamiento
        listaComputadoras.append(computadora)
    return jsonify({'computadora':listaComputadoras})