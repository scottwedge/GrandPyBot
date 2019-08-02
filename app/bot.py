from flask import Flask
from flask import render_template, request
import urllib.parse
import requests
import random


class bot():
    """
    Class to make the bots logics, and methods to communicate 
    with the front end querys.
    """
    def __init__(self):
        """
        Load lists contents as filters helps
        """
        self.welcoming = ['bonjour', 'Vraiment', 'non', 'Oui']
        self.successResp = ['et voila', 'ui', 'l\'adresse est la suivante']
        self.faildResp = ['Malheuresement Pas d\'histoire']



    def messageBot(self, statu):
        
        self.statu = statu
        self.msg = ''
        if self.statu == 'w':
            self.msg = random.choice(self.welcoming)
        elif statu == 's':
            self.msg = random.choice(self.successResp)
        elif statu == 'f':
            self.msg = random.choice(self.faildResp)
        else: 
            print('Specifie the statu please')
        return self.msg
