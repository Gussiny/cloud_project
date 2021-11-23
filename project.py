from mpi4py import MPI
import os
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from google.cloud import firestore, storage
from math import pi, sqrt
from subprocess import check_output

comm = MPI.COMM_WORLD
r = comm.Get_rank()

app = Flask(__name__)
CORS(app)

@app.route("/")
def hello():
    return render_template('index.html')

@app.route('/cilindro', methods = ['POST'])
def getCilindro():
    if request.method == 'POST':
        radio = float(request.form['radio'])
        altura = float(request.form['altura'])
        result = []

        if r == 0:
            ### AREA
            area = (2 * radio * pi) * (altura + radio)
            comm.send( area, dest = 1, tag = 11)
        elif r == 1:
            ### VOLUMEN
            volumen = ((radio ** 2) * pi * altura)
            result.append( round(volumen, 2) )
            area = comm.recv( source = 0, tag = 11)
            result.append( round(area, 2) )

        response = jsonify({'Resultados': result})
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response

@app.route('/cubo', methods = ['POST'])
def getCubo():
    if request.method == 'POST':
        altura = float(request.form['altura'])
        result = []

        if r == 0:
            area = ( 6 * (altura ** 2) )
            comm.send( area, dest = 1, tag = 11)
        elif r == 1:
            volumen = (altura ** 3)
            result.append( round(volumen, 2) )
            area = comm.recv( source = 0, tag = 11)
            result.append( round(area, 2) )
        
        response = jsonify({'Resultados': result})
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response

@app.route('/esfera', methods = ['POST'])
def getEsfera():
    if request.method == 'POST':
        radio = float(request.form['radio'])
        result = []

        if r == 0:
            area = ( 4 * pi * (radio ** 2) )
            comm.send( area, dest = 1, tag = 11)
        elif r == 1:
            volumen = ( 4 * pi  * (radio ** 3) ) / 3
            result.append( round(volumen, 2) )
            area = comm.recv( source = 0, tag = 11)
            result.append( round(area, 2) )
        
        response = jsonify({'Resultados': result})
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response

@app.route('/cono', methods = ['POST'])
def getCono():
    if request.method == 'POST':
        
        altura = float(request.form['altura'])
        radio = float(request.form['radio'])
        result = []
        
        if r == 0:
            g = sqrt((altura ** 2) + (radio ** 2))
            area = ( (pi * (radio ** 2)) + ( g * pi * radio) )
            comm.send( area, dest = 1, tag = 11)
        elif r == 1:
            volumen = ( (radio ** 2) * pi  * altura ) / 3
            result.append( round(volumen, 2) )
            area = comm.recv( source = 0, tag = 11)
            result.append( round(area, 2) )
        
        response = jsonify({'Resultados': result})
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response

@app.route('/prisma', methods = ['POST'])
def getPrisma():
    if request.method == 'POST':
        
        altura = float(request.form['altura'])
        ancho = float(request.form['ancho'])
        largo = float(request.form['largo'])
        result = []
        
        if r == 0:
            area = ( 2 * altura  * (ancho + largo) + (2 * ancho * largo) )
            comm.send( area, dest = 1, tag = 11)
        elif r == 1:
            volumen = ancho * largo * altura
            result.append( round(volumen, 2) )
            area = comm.recv( source = 0, tag = 11)
            result.append( round(area, 2) )
        
        response = jsonify({'Resultados': result})
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response

if __name__ == "__main__":
    app.run(host='0.0.0.0', port="5000")