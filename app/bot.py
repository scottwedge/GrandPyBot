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
                # listData = data.split()
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
        apikey = ""

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
        adresse = self.stopWd()
        adresse = adresse.replace(" ", "")
        apikey = ""
        lat = code[0]
        longe = code[1]

        base_url = "https://www.google.com/maps/embed/v1/view?key={}&center={},{}&zoom=18&maptype=satellite".format(
            apikey, lat, longe
        )
        return base_url

    def MediaWiki(self):
        """A Moethod to get a storie about the place from mediawiki
         and a random answer if the response was not well explained
         or there is an error
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

        return print(response)
