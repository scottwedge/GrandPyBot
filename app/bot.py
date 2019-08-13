import os
from flask import Flask
from flask import render_template, request
import urllib.parse
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
        
    def splitStp(self):
        """
        Method to open and read the data in the stopwords file
        """
        try:
            with open('./app/stopwords.txt')as file:
                data = file.read()
                listData = data.split()
            return listData
        except:
            with open('stopwords.txt')as file:
                data = file.read()
                listData = data.split()
            return listData

            
    def stopWd(self):
        """
        metod to chek if the input's elts are existing
        in the stop words or not, to return a cleaner input
        """
        self.splitStp()
        cleanWords=[]
        response = self.ask.split()
        for elt in response:
            if elt not in self.splitStp():
                cleanWords.append(elt)
        #print(' '.join(cleanWords))
        return(' '.join(cleanWords))

    def MediaWiki(self):
        """A Moethod to get a storie about the place from mediawiki
         and a explnation if the response dont exist
        """
        

        base_url = "http://fr.wikipedia.org/w/api.php"
        params_url = {"action": "opensearch",
                  "search": self.stopWd(),
                  "limit": "1",
                  "namespace": "0",
                  "format": "json"}
        
        self.ResultUrl = requests.get(url=base_url, params=params_url)
        #print(self.ResultUrl.url)
        try:
            answer = self.ResultUrl.json()[2][0]
            return  answer
        except:
            error = "Désolé mon amis J'ai peut etre pas compris ta question ou, l'endroit que tu chere na aucune histoire :'("
            return error
       


    def GooglMapFrame(self):
        """Geting the localisation on the map"""
        
        
        base_url = "https://www.google.com/maps/search/?api=1&query="+self.stopWd()
        print(base_url)
        
         
        






    