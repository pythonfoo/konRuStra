#!/usr/bin/env python 
#-*- coding: utf-8 -*-
""" Game objects for konRuStra """
__author__ = "oerb"
__copyright__ = "GPL 2013"
__license__ = "GPL" 

import uuid # UniceIdentify Objects


class Player(object):
    """ Dataclass for every Player to store and give data to every Player"""
    def __init__(self):

        self._playerId = uuid.uuid4()
        self._name = ""

    @property 
    def playerId(self): 
        " Returns the Player UUID"    
        return self._playerId 

    @property 
    def name(self): 
            return self._name 

    @name.setter 
    def name(self, value):
        if type(value) == str:
            self._name = value
        else:
            raise Exception("Error Playername has to be Type Str")

class Bot(Player):
    """ Used for Bots in the AI """
    pass

class gamer(Player):
    "Real Person that Plays"
    def __init__(self):
        super(gamer, self).__init__()
        self._hp = 0 # Health Points
        self._pp = 0 # Perseverance Point

    @property 
    def hp(self): 
        "Health Point"
        return self._hp 

    @hp.setter 
    def hp(self, value):
        if type(value) == int:
            self._hp = value
        else:
            raise Exception("Error hp has to be type int")

    @property 
    def pp(self):
        "Perseverance Point"
        return self._pp

    @pp.setter 
    def pp(self, value):
        if type(value) == int:
            self._pp = value
        else:
            raise Exception("Error pp has to be type int")






def main():
    testPlayer = gamer()
    testPlayer.name = "Oerb"
    testPlayer.hp = 20
    print testPlayer.playerId, testPlayer.name, testPlayer.hp, testPlayer.pp


if __name__ == "__main__":
    main()







