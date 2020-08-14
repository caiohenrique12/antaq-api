from flask import Flask, jsonify
from flask_cors import CORS
from antaq import Antaq

app = Flask('antaq')
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

@app.route('/')
def root_path():
  return 'Welcome Page'

@app.route('/atracacao/<year>', methods=['GET'])
def atracacao_data(year):
  antaq = Antaq(year=year)
  return jsonify({
    'status': 'success',
    'data': antaq.return_atracao()
  })
  
@app.route('/carga/<year>', methods=['GET'])
def carga_data(year):
  antaq = Antaq(year=year)
  return jsonify({
    'status': 'success',
    'data': antaq.return_carga()
  })

app.run()
