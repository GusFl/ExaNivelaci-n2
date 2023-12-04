from flask import Blueprint, request, render_template, redirect,url_for
from models import Carne
from forms import CarneForm
from app import db

appcarne = Blueprint('appcarne',__name__,template_folder="templates")

@appcarne.route('/indexCarne')
def inicio():
    carnes = Carne.query.all()
    totalDeCarnes = Carne.query.count()
    return render_template('indexCarne.html',carnes =carnes, totalDeCarnes = totalDeCarnes)

@appcarne.route('/agregarCarne',methods=["GET","POST"])
def agregar():
    carne = Carne()
    carneForm = CarneForm(obj=carne)
    if request.method == "POST":
        if carneForm.validate_on_submit():
            carneForm.populate_obj(carne)
            db.session.add(carne)
            db.session.commit()
            return redirect(url_for('appcarne.inicio'))
    return render_template('agregarCarne.html',forma=carneForm)

@appcarne.route('/editarCarne/<int:id>',methods=["GET","POST"])
def editar(id):
    carne = Carne.query.get_or_404(id)
    carneForm = CarneForm(obj=carne)
    if request.method == "POST":
        if carneForm.validate_on_submit():
            carneForm.populate_obj(carne)
            db.session.commit()
            return redirect(url_for('appcarne.inicio'))
    return render_template('editarCarne.html',forma=carneForm)

@appcarne.route('/detalleCarne/<int:id>')
def detalle(id):
    carne = Carne.query.get_or_404(id)
    return render_template('detalleCarne.html',carne = carne)

@appcarne.route('/eliminarCarne/<int:id>')
def eliminar(id):
    carne = Carne.query.get_or_404(id)
    db.session.delete(carne)
    db.session.commit()
    return redirect(url_for('appcarne.inicio'))