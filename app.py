from flask import Flask
from flask_mysqldb import MySQL, MySQLdb
from flask import request
from flask import render_template
from flask_cors import CORS, cross_origin

from flask import url_for, flash, redirect
from werkzeug.exceptions import abort

from sonido import *
from asyncio import get_event_loop
from multiprocessing.connection import wait

import mysql.connector

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '123456'
app.config['MYSQL_DB'] = 'hotelregister'

mysql = MySQL(app)

cors = CORS(app)

app.secret_key='secretkey'

#############################################

@app.route('/')
@cross_origin()
def home():
    return render_template("index.html")

@app.route('/hotel/5estrellas')
@cross_origin()
def hotels5():
    return render_template("Hoteles5.html")

@app.route('/hotel/hotelsnew')
@cross_origin()
def hotelsnew():
    return render_template("Hotelesnew.html")

@app.route('/hotel/contacts')
@cross_origin()
def contacts():
    return render_template("contacts.html")

############################################

@app.route('/hotel/hotel1')
@cross_origin()
def hotel1():
    return render_template("hotel1.html")

@app.route('/hotel/hotel1/reserva', methods=('GET', 'POST'))
@cross_origin()
def reserva1():
    if request.method == 'POST':
        Apellidos = request.form['Apellidos']
        Nombres = request.form['Nombres']
        Email = request.form['Email']
        Celular = request.form['Celular']
        Habitaciones = request.form['Habitaciones']
        Descripcion = request.form['Descripcion']

        cursor=mysql.connection.cursor()
        cursor.execute('INSERT INTO guests_h1 (Apellidos, Nombres, Email, Celular, Habitaciones, Descripcion) values (%s,%s,%s,%s,%s,%s)', (Apellidos, Nombres, Email, Celular, Habitaciones, Descripcion))
        mysql.connection.commit()
        flash("Add Guest")
        return  redirect(url_for('hotel1'))

    return render_template("Reserva1.html")

@app.route('/hotel/hotel1/calificacion', methods=('GET', 'POST'))
@cross_origin()
def calificacion1():
    if request.method == 'POST':
        Apellidos = request.form['Apellidos']
        Nombres = request.form['Nombres']
        Email = request.form['Email']
        Mensaje = request.form['Mensaje']
        Calificacion = request.form['Calificacion']

        cursor=mysql.connection.cursor()
        cursor.execute('INSERT INTO rateus (Apellidos, Nombres, Email, Mensaje, Calificacion) values (%s,%s,%s,%s,%s)', (Apellidos, Nombres, Email, Mensaje, Calificacion))
        mysql.connection.commit()
        flash("Add Rate")
        return  redirect(url_for('hotel1'))
    return render_template("Calificacion1.html")

@app.route('/hotel/hotel1/contactus', methods=('GET', 'POST'))
@cross_origin()
def contactus1():
    if request.method == 'POST':
        Apellidos = request.form['Apellidos']
        Nombres = request.form['Nombres']
        Email = request.form['Email']
        Mensaje = request.form['Mensaje']

        cursor=mysql.connection.cursor()
        cursor.execute('INSERT INTO contactus (Apellidos, Nombres, Email, Mensaje) values (%s,%s,%s,%s)', (Apellidos, Nombres, Email, Mensaje))
        mysql.connection.commit()
        flash("Add Form")
        return  redirect(url_for('hotel1'))
    return render_template("contactanos1.html")

#############################################

valor=["Presiona el boton de play para iniciar",0]
app.secret_key='mysecretkey'
dic_cantidad={'un':'1','uno':'1','dos':'2','tres':'3','cuatro':'4','cinco':'5','seis':'6','siete':'7','ocho':'8','nueve':'9','cero':'0'}
dic_productos=['cebolla','zanahoria','papa','aceite']
dic_u_medidas=['kilo','litro']
valor = []
@app.route('/transcripcion',methods = ['POST','GET'])
def transcripcion():
    if(loop.is_running() and (not estado[0])):
        while(loop.is_running()):
            resultados=[]
        resultados=[]
        for i in guardado:
            menor=i.lower()
            diack=menor[:-1]
            resultados.append(diack.split())
        for j in resultados:
            lista=["-","-","-"]
            for i in j:
                if(i in dic_cantidad):
                    if(lista[0]=="-"):
                        lista[0]=""
                    lista[0]=lista[0]+dic_cantidad[i]
                elif (i in dic_u_medidas):
                    lista[1]=i
                elif (i[:-1] in dic_u_medidas):
                    lista[1]=i[:-1]
                elif (i in dic_productos):
                    lista[2]=i
                elif (i[:-1] in dic_productos):
                    lista[2]=i[:-1]
            valor.append(lista)
    elif(estado[0] and (not loop.is_running())):
        guardado.clear()
        loop.run_until_complete(Recibir_Enviar())
    return render_template('Transcribe.html', texto=guardado,valores=valor)

@app.route('/transenviplay')
def transenviplay():
    estado[0]=True
    return redirect(url_for('transcripcion'))

@app.route('/transenvistop')
def transenvistop():
    estado[0]=False
    return redirect(url_for('transcripcion'))

#############################################

if __name__ == "__main__":
    app.run(debug=True)
