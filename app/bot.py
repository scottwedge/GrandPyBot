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
        print(cleanWords)
        return(' '.join(cleanWords))
         
        






    