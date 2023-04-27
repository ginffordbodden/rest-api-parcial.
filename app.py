
from flask import Flask
import flask
import pandas as pd

app = Flask(__name__)

 
df = pd.read_excel('api.xls')

datos = df.to_dict(orient='records')

@app.route('/datos', methods=['GET'])
def get_datos():
    pais = 'Panama'
    indicador = 'Indicator'


    datos_filtrados = [dato for dato in datos if dato['Country Name'] == pais and dato['Indicator'] == indicador]


    return flask.jsonify(datos_filtrados)

if __name__ == '__main__':
    app.run(debug=True)