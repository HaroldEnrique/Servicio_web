import os
import re
import json


class Fechas:

"""clase para las fechas del servicio web"""
    def __init(self):
        try:#DE https://stackoverflow.com/questions/2835559/pasring-values-from-a-json-file
            if os.path.exists('fechas.json'):
                path='fechas.json'
            elif os.path.exists('/data/fechas.json'):
                path='/data/fechas.json'
            elif os.path.exists('./data/fechas.json'):
                path='./data/fechas.json'
            elif os.path.exists('../data/fechas.json'):
                path='../data/fechas.json'
            else:
                raise IOError("No se encuentra 'fechas.json'")

            with open(path) as data_file:
                self.fechas=json.load(data_file)
        except IOError as fallo:
            print("Error {:s} leyendo fechas.json".format(fallo))


    def todos_fechas(self):
        return self.fechas

    def cuantos(self):
        return len(self.fechas['fechas'])

    def uno(self, fecha_id):
        if()

