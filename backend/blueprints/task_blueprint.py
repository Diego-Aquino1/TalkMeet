from flask import Flask
from flask import Blueprint
from flask import request
from flask import jsonify
from flask import render_template

from flask_cors import CORS, cross_origin # para que no genere errores de CORS al hacer peticiones

from backend.models.task_model import TaskModel

task_blueprint = Blueprint('hotel_blueprint', __name__)

model = TaskModel()


@task_blueprint.route('/hotel/add_rate', methods=['POST'])
@cross_origin()
def create_taskru():
    content = model.add_rate(request.json['Apellidos'], request.json['Nombres'], request.json['Email'], request.json['Mensaje'], request.json['Calificacion'])
    return jsonify(content)

@task_blueprint.route('/hotel/delete_rate', methods=['POST'])
@cross_origin()
def delete_taskru():
    return jsonify(model.delete_rate(int(request.json['Idrateus'])))

@task_blueprint.route('/hotel/get_rate', methods=['POST'])
@cross_origin()
def taskru():
    return jsonify(model.get_rate(int(request.json['Idrateus'])))

@task_blueprint.route('/hotel/get_rates', methods=['POST'])
@cross_origin()
def tasksru():
    return jsonify(model.get_rates())


#######################################


@task_blueprint.route('/hotel/add_form', methods=['POST'])
@cross_origin()
def create_taskcu():
    content = model.add_form(request.json['Apellidos'], request.json['Nombres'], request.json['Email'], request.json['Mensaje'])
    return jsonify(content)

@task_blueprint.route('/hotel/delete_form', methods=['POST'])
@cross_origin()
def delete_taskcu():
    return jsonify(model.delete_form(int(request.json['Idcontactus'])))

@task_blueprint.route('/hotel/get_form', methods=['POST'])
@cross_origin()
def taskcu():
    return jsonify(model.get_form(int(request.json['Idcontactus'])))

@task_blueprint.route('/hotel/get_forms', methods=['POST'])
@cross_origin()
def taskscu():
    return jsonify(model.get_forms())


#######################################


@task_blueprint.route('/hotel/add_guest_h1', methods=['POST'])
@cross_origin()
def create_taskh1():
    content = model.add_guest1(request.json['Apellidos'], request.json['Nombres'], request.json['Email'], request.json['Celular'], request.json['Habitaciones'], request.json['Descripcion'])
    return jsonify(content)

@task_blueprint.route('/hotel/delete_guest_h1', methods=['POST'])
@cross_origin()
def delete_taskh1():
    return jsonify(model.delete_guest1(int(request.json['ID'])))

@task_blueprint.route('/hotel/get_guest_h1', methods=['POST'])
@cross_origin()
def taskh1():
    return jsonify(model.get_guest1(int(request.json['ID'])))

@task_blueprint.route('/hotel/get_guests_h1', methods=['POST'])
@cross_origin()
def tasksh1():
    return jsonify(model.get_guests1())

#######################################