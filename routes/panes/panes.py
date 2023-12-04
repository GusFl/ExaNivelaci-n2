from flask import Blueprint, request,jsonify
from models import Pan
from app import db

apppan= Blueprint('apppan',__name__,template_folder="templates")

@apppan.route('/pan/agregar',methods={'POST'})
def agregaJuego():
    try:
        json = request.get_json()
        pan = Pan()
        pan.tipo = json['tipo']
        pan.descripcion = json['descripcion']
        pan.precio = json['precio']
        pan.tamaño = json['tamaño']
        db.session.add(pan)
        db.session.commit()
        return jsonify({"status":200, "mensaje":"pan agregado"})
    except Exception as ex:
        return jsonify({"status":400,"mensaje":ex})

@apppan.route('/pan/editar',methods={"POST"})
def editaJuego():
    try:
        json = request.get_json()
        pan = Pan.query.get_or_404(json['id'])
        pan.tipo = json['tipo']
        pan.descripcion = json['descripcion']
        pan.precio = json['precio']
        pan.tamaño = json['tamaño']
        db.session.commit()
        return jsonify({'status':"OK",'mensaje':"pan modificado"})
    except Exception as ex:
        return jsonify({"status":"ERROR","mensaje":ex})
    
@apppan.route('/pan/eliminar',methods={"POST"})
def eliminaJuego():
    try:
        json = request.get_json()
        pan = Pan.query.get_or_404(json['id'])
        db.session.delete(pan)
        db.session.commit()
        return jsonify({'status':"OK",'mensaje':"pan eliminado"})
    except Exception as ex:
        return jsonify({"status":"ERROR","mensaje":ex})

@apppan.route('/pan/obtener',methods={"GET"})
def obtenerJuego():
    panes = Pan.query.all()
    listaPanes=[]
    for r in panes:
        pan = {}
        pan['nombre'] = r.nombre
        pan['descripcion'] = r.descripcion
        pan['precio'] = r.precio
        pan['plataforma'] = r.plataforma
        listaPanes.append(pan)
    return jsonify({'pan':listaPanes})