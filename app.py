from flask import Flask, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

def checaDados(dados, nome):
    if (nome == "soma" or nome == "subtrai" or nome == 'multiplica'):
        if "x" not in dados or "y" not in dados:
            return 301
        else:
            return 200
    else:
        if (nome == "divide"):
            if "x" not in dados or "y" not in dados:
                return 301
            else:
                if (int(dados['y']) == 0):
                    return 302
                else:
                    return 200
         

class Soma(Resource):
    def post(self):
        # se to aqui, o recurso Soma foi solicitado usando o 
        # método POST
        dadosPostados = request.get_json()

        # if 'x' not in dadosPostados or 'y' not in dadosPostados:
        #     return "ERRO, VERIFIQUE OS PARÂMETROS, CUIDADO COM MAIUSCULAS", 305
        codigo_status = checaDados(dadosPostados, "soma")

        if (codigo_status != 200):
            meuJson = {
                'Mensagem': "Um erro ocorreu, verifique os parametros",
                'Código de estatus': codigo_status
            }
            return meuJson

        x = int(dadosPostados['x'])
        y = int(dadosPostados['y'])
        z = x + y
        meuJson = {
            'soma': z,
            'Código de estatus': codigo_status
        }
        return meuJson


class Diminui(Resource):
    def post(self):
        dadosPostados = request.get_json()

        codigo_status = checaDados(dadosPostados, "subtrai")
        #agora precisamos montar os JSON para o retorno de dados
        if (codigo_status != 200):
            meuJson = {
                'Mensagem': "Um erro ocorreu, verifique os parametros",
                'Código de estatus': codigo_status
            }
            return meuJson
             
        x = int(dadosPostados['x'])
        y = int(dadosPostados['y'])
        z = x - y
        meuJson = {
            'subtracao': z,
            'Código de estatus': codigo_status
        }
        return meuJson
        
class Multiplica(Resource):
    def post(self):
        dadosPostados = request.get_json()

        codigo_status = checaDados(dadosPostados, "multiplica")
        #agora precisamos montar os JSON para o retorno de dados
        if (codigo_status != 200):
            meuJson = {
                'Mensagem': "Um erro ocorreu, verifique os parametros",
                'Código de estatus': codigo_status
            }
            return meuJson
             
        x = int(dadosPostados['x'])
        y = int(dadosPostados['y'])
        retorno = x * y
        meuJson = {
            'Multiplicação': retorno,
            'Código de estatus': codigo_status
        }
        return meuJson


class Divide(Resource):
    def post(self):
        dadosPostados = request.get_json()

        codigo_status = checaDados(dadosPostados, "divide")
        #agora precisamos montar os JSON para o retorno de dados
        if (codigo_status != 200):
            if (codigo_status == 302):
                meuJson = {
                'Mensagem': "Não existe divisão por Zero, reveja as entradas!",
                'Código de estatus': codigo_status
                }
                return meuJson
            else:
                meuJson = {
                    'Mensagem': "Um erro ocorreu, verifique os parametros",
                    'Código de estatus': codigo_status
                }
                return meuJson
             
        x = int(dadosPostados['x'])
        y = int(dadosPostados['y'])
        retorno = (x*1.0) / y
        meuJson = {
            'divisão': retorno,
            'Código de estatus': codigo_status
        }
        return meuJson

api.add_resource(Soma, '/soma')
api.add_resource(Diminui, '/diminui')
api.add_resource(Multiplica, '/multiplica')
api.add_resource(Divide, '/divide')

@app.route('/')
def hola_baleia():
    return "Holá mundo!"

@app.route('/bebito')
def hola_urso():
    return "Exibindomum endpoint diferente"

if __name__=="__main__":
    app.run(debug=True)