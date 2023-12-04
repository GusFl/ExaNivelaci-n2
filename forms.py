from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class PanForm(FlaskForm):
    tipo = StringField('Tipo',validators=[DataRequired()]) #Validators hace obligatorio el campo 
    descripcion = StringField('Descripcion',validators=[DataRequired()])
    precio = StringField('precio',validators=[DataRequired()]) 
    tamaño= StringField('tamaño',validators=[DataRequired()]) 
    enviar =  SubmitField('Enviar')

class CarneForm(FlaskForm):
    nombre = StringField('Nombre',validators=[DataRequired()]) #Validators hace obligatorio el campo 
    descripcion = StringField('Descripcion',validators=[DataRequired()])
    precio = StringField('Precio',validators=[DataRequired()]) 
    peso = StringField('Peso',validators=[DataRequired()]) 
    enviar =  SubmitField('Enviar')

class CarroForm(FlaskForm):
    nombre = StringField('Nombre',validators=[DataRequired()]) #Validators hace obligatorio el campo 
    kilometraje = StringField('Kilometraje',validators=[DataRequired()])
    precio = StringField('Precio',validators=[DataRequired()]) 
    marca = StringField('Marca',validators=[DataRequired()]) 
    enviar =  SubmitField('Enviar')

class ComputadoraForm(FlaskForm):
    nombre = StringField('Nombre',validators=[DataRequired()]) #Validators hace obligatorio el campo 
    marca = StringField('Marca',validators=[DataRequired()])
    ram  = StringField('Ram',validators=[DataRequired()]) 
    almacenamiento = StringField('Almacenamiento',validators=[DataRequired()]) 
    enviar =  SubmitField('Enviar')

class BebidaForm(FlaskForm):
    nombre = StringField('Nombre',validators=[DataRequired()]) #Validators hace obligatorio el campo 
    descripcion = StringField('Descripcion',validators=[DataRequired()])
    precio = StringField('Precio',validators=[DataRequired()]) 
    color = StringField('Color',validators=[DataRequired()]) 
    enviar =  SubmitField('Enviar')