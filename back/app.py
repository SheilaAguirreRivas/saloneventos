from flask import Flask ,jsonify ,request
from flask_cors import CORS      
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from datetime import datetime

app = Flask(__name__)
CORS(app)

#BBDD
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:@localhost/salon_eventos'
#'mysql+pymysql://SheiAguirreR:sqlmyShei0803!@SheiAguirreR.mysql.pythonanywhere-services.com/SheiAguirreR$salon_eventos'
#'mysql+pymysql://root:@localhost/salon_eventos'
#user:clave@URLBBDD/nombreBBDD
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False #none
db= SQLAlchemy(app)   #crea el objeto db de la clase SQLAlquemy
ma=Marshmallow(app)   #crea el objeto ma de de la clase Marshmallow


class Evento(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fechaEvento = db.Column(db.Date)
    nombreApellido = db.Column(db.String(100))
    numContacto = db.Column(db.Integer())
    tipoEvento = db.Column(db.String(50))
    valorSalon = db.Column(db.Integer())
    cantInvitados = db.Column(db.Integer())
    responsable = db.Column(db.String(100))

    def __init__(self, fechaEvento, nombreApellido, numContacto, tipoEvento, valorSalon, cantInvitados, responsable ):
        self.fechaEvento = fechaEvento
        self.nombreApellido = nombreApellido
        self.numContacto = numContacto
        self.tipoEvento = tipoEvento
        self.valorSalon = valorSalon
        self.cantInvitados = cantInvitados
        self.responsable = responsable
        
#Resto de las tablas

with app.app_context():
    db.create_all()  # aqui crea todas las tablas
#  ********************
class EventoSchema(ma.Schema):
    class Meta:
        fields=('id', 'fechaEvento', 'nombreApellido', 'numContacto', 'tipoEvento', 'valorSalon', 'cantInvitados', 'responsable')

evento_schema=EventoSchema()            # El objeto producto_schema es para traer un producto
eventos_schema=EventoSchema(many=True)  # El objeto productos_schema es para traer multiples registros de producto

@app.route('/eventos', methods=['GET'])
def get_eventos():
    all_eventos = Evento.query.all()
    result = eventos_schema.dump(all_eventos)
    return jsonify(result)

@app.route('/eventos/<id>',methods=['GET'])
def get_evento(id):
    evento=Evento.query.get(id)
    return evento_schema.jsonify(evento)   # retorna el JSON de un producto recibido como parametro

@app.route('/eventos/<id>',methods=['DELETE'])
def delete_evento(id):
    evento=Evento.query.get(id)
    db.session.delete(evento)
    db.session.commit()
    return evento_schema.jsonify(evento)

@app.route('/eventos', methods=['POST']) #Crear un registro
def create_evento():
    fechaEvento=request.json['fechaEvento']
    nombreApellido=request.json['nombreApellido']
    numContacto=request.json['numContacto']   
    tipoEvento=request.json['tipoEvento']
    valorSalon=request.json['valorSalon']
    cantInvitados=request.json['cantInvitados']
    responsable=request.json['responsable']
    nuevo_evento = Evento(fechaEvento, nombreApellido, numContacto, tipoEvento, valorSalon, cantInvitados, responsable)
    db.session.add(nuevo_evento)
    db.session.commit()
    return evento_schema.jsonify(nuevo_evento)

@app.route('/eventos/<id>',methods=['PUT']) #MODIFICAR 
def update_evento(id):
    evento = Evento.query.get(id)   
    fechaEvento = request.json['fechaEvento']
    nombreApellido = request.json['nombreApellido']
    numContacto = request.json['numContacto']   
    tipoEvento = request.json['tipoEvento']
    valorSalon = request.json['valorSalon']
    cantInvitados = request.json['cantInvitados']
    responsable = request.json['responsable']
    
    evento.fechaEvento = fechaEvento
    evento.nombreApellido = nombreApellido
    evento.numContacto = numContacto
    evento.tipoEvento = tipoEvento
    evento.valorSalon = valorSalon
    evento.cantInvitados = cantInvitados
    evento.responsable = responsable
    

    db.session.commit()
    return evento_schema.jsonify(evento)

if __name__ == '__main__':
  app.run(debug=True, port=5000)
#if __name__ == '__main__':
 #  app.run(debug=True, port=5000)