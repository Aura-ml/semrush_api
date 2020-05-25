
# coding: utf-8

import requests
import json



class SemrushCps:
    def __init__(self, url=None, motcles=None, payload=None):
        self.url = url
        self.mot_cles = motcles
        self.payload = payload
        self.data = None

    def recuperer_positionement(self):
        # args1: url ou nom de domaine
        if self.url is None:
            print("url undefine")
        else:
            print({"value": requests.get(self.url).text})

    def sugestion_mot_cles(self):
        if self.mot_cles is None:
            print("liste de mots manquante")
        else:
            print("yep")

    def export_to_json(self):
        if data is None:
            print("aucune valeur a uploader")
        else:
            print("upload")
                                            ########## new version ###############





