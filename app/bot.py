import os
from flask import Flask
from flask import render_template, request
import urllib.parse
from pprint import pprint
import requests
import random


class Bot:
    """
    Class to make the bots logics, and methods to communicate 
    with the front end querys.
    """

    def __init__(self, ask):
        """
        Load lists contents as filters helps
        # """
        self.ask = ask
        self.latitude = ""
        self.longetude = ""

    def splitStp(self):
        """
        Method to open and read the data in the stopwords file
        """
        try:
            with open("./app/stopwords.txt") as file:
                data = file.read()

            return data
        except:
            error = "Un erreur s'est produit"
            return error

    def stopWd(self):
        """
        metod to chek if the input's elts are existing
        in the stop words or not, to return a cleaner input
        """
        self.splitStp()
        cleanWords = []
        response = self.ask.split()
        for elt in response:
            if elt not in self.splitStp():
                cleanWords.append(elt)
        print(" ".join(cleanWords))
        return " ".join(cleanWords)

    def geoCode(self):
        """Get the Geaoinformations about the user's task entred"""
        sendQts = self.stopWd()
        apikey = os.environ.get("API")

        base_url = (
            "https://maps.googleapis.com/maps/api/geocode/json?address="
            + sendQts
            + "&key="
            + apikey
        )
        request = requests.get(base_url)
        jsRequest = request.json()
        target = jsRequest["results"]

        points = []
        for elt in target:
            points = elt["geometry"]["location"]
        self.latitude = points["lat"]
        self.longetude = points["lng"]
        return [self.latitude, self.longetude]

    def GooglMaplink(self):
        """Geting the localisation on the map"""
        code = self.geoCode()
        # adresse = self.stopWd()
        # adresse = adresse.replace(" ", "")
        apikey = os.environ.get("API")
        lat = code[0]
        longe = code[1]

        base_url = "https://www.google.com/maps/embed/v1/view?key={}&center={},{}&zoom=18&maptype=satellite".format(
            apikey, lat, longe
        )
        return base_url

    def wiki_Code_Loc(self):
        """
        Method getting the whole localisation of the place based on geoInformationdelivred by
        the geoCode method 
        """
        code = self.geoCode()
        lat = code[0]
        longe = code[1]
        url = "https://fr.wikipedia.org/w/api.php"

        latitude = lat
        longitude = longe

        params = {
            "format": "json",  # format de la réponse
            "action": "query",  # action à réaliser
            "list": "geosearch",  # méthode de recherche
            "gsradius": 10000,  # rayon de recherche autour des coordonnées GPS fournies (max 10'000 m)
            "gscoord": f"{latitude}|{longitude}",  # coordonnées GPS séparées par une barre verticale
        }
        response = requests.get(url, params=params)

        if response.status_code == 200:
            data = response.json()
            return data
        else:
            data = {"query": {"geosearch": []}}
            print("Error")

        return data

    def media_Wiki_Resp(self):
        """A Moethod to get a storie about the place from mediawiki
         and a random answer if the response was not well explained
         or there is an error
        """
        data = self.wiki_Code_Loc()
        page_id = data["query"]["geosearch"][0]["pageid"]
        url = "https://fr.wikipedia.org/w/api.php"

        params = {
            "format": "json",  # format de la réponse
            "action": "query",  # action à effectuer
            "prop": "extracts|info",  # Choix des propriétés pour les pages requises
            "inprop": "url",  # Fournit une URL complète, une URL de modification, et l’URL canonique de chaque page.
            "exchars": 1200,  # Nombre de caractères à retourner
            "explaintext": 1,  # Renvoyer du texte brut (éliminer les balises de markup)
            "pageids": page_id,
        }

        response = requests.get(url, params=params)
        if response.status_code == 200:
            data = response.json()
            return data["query"]["pages"][str(page_id)]["extract"]
        else:
            return "Error"
