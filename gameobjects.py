#!/usr/bin/env python 
#-*- coding: utf-8 -*-
""" Game objects for konRuStra """
__author__ = "oerb"
__copyright__ = "GPL 2013"
__license__ = "GPL" 

import uuid # UniceIdentify Objects

class PlayerHelper(object):
    "gives Methods to get default Figures and other Figuremanipulations"
    def __init__(self):
        self._playerlist = {}

    def _player_add(self, playervalue):
        "add Player to Playerlist"
        if isinstance(playervalue,Player):
            self._playerlist[playervalue.playerId] = playervalue
        else:
            raise Exception("Error type Player hast to be Player Object")
    
    def _player_remove(self, playervalue): 
        "removes Player from Playerlist"
        if isinstance(playervalue, Player):
            self._playerlist.pop(playervalue.playerId, None)
        else:
            raise Exception("Error type Player hast to be Player Object")

    def get_Playerlist(self):
        "returns intern Playerlist - must be replaced by inteligent Methods"
        #TODO: nomore return of intern Playerlist just uses Methods to manipulate
        return self._playerlist

    def get_new_Soldier(self):
        "returns a new Soldier with defaults"
        soldier = gamer()
        soldier.hp = 1250
        soldier.pp = 250
        soldier.wd = 1
        soldier.soa = 50
        soldier.hpReg = 3
        soldier.ppReg = 1
        soldier.price = 500
        soldier.ep = 0
        soldier.playertyp = "soldier"
        self._player_add(soldier)
        return soldier

    def get_new_Robber(self):
        "returns a new Robber with defaults"
        robber = gamer()
        robber.hp = 750
        robber.pp = 750 
        robber.wd = 2
        robber.soa = 45
        robber.hpReg = 2
        robber.ppReg = 2
        robber.price = 500
        robber.ep = 0
        robber.playertyp = "robber"
        self._player_add(robber)
        return robber

    def get_new_Wizard(self):
        "returns a new Wizard with defaults"
        wizard = gamer()
        wizard.hp = 1000
        wizard.pp = 500
        wizard.wd = 3
        wizard.soa = 40
        wizard.hpReg = 1
        wizard.ppReg = 3
        wizard.price = 500
        wizard.ep = 0
        wizard.palyertyp = "wizard"
        self._player_add(wizard)
        return wizard

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
        self._wd = 0 # Weapon Distance
        self._soa = 0 # Strength of arms
        self._hpReg = 0 # Health Point Recharge
        self._ppReg = 0 # Perseverance Point Recharge
        self._price = 0 # Price
        self._level = 0 # Level
        self._ep = 0 # what ever it is ... ask DoDo
        self._playertyp = 0 # 1 = soldier, 2 = robber, 3 = wizard 

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

    @property 
    def wd(self):
        "Weapon Distance"
        return self._wd

    @wd.setter 
    def wd(self, value):
        if type(value) == int:
            self._wd = value

        else:
            raise Exception("Error wd has to be type int")



    @property 
    def soa(self):
        "Strength of arms"
        return self._soa

    @soa.setter 
    def soa(self, value):
        if type(value) == int:
            self._soa = value

        else:
            raise Exception("Error soa has to be type int")


    @property 
    def hpReg(self):
        "Health Point Recharge"
        return self._hpReg

    @hpReg.setter 
    def hpReg(self, value):
        if type(value) == int:
            self._hpReg = value

        else:
            raise Exception("Error hpReg has to be type int")

    @property 
    def ppReg(self):
        "Perseverance Point Recharge"
        return self._ppReg

    @ppReg.setter 
    def ppReg(self, value):
        if type(value) == int:
            self._ppReg = value

        else:
            raise Exception("Error ppReg has to be type int")


    @property 
    def price(self):
        "Price"
        return self._price

    @price.setter 
    def price(self, value):
        if type(value) == int:
            self._price = value

        else:
            raise Exception("Error price has to be type int")


    @property 
    def level(self):
        "Level"
        return self._level

    @level.setter 
    def level(self, value):
        if type(value) == int:
            self._level = value

        else:
            raise Exception("Error level has to be type int")


    @property 
    def ep(self):
        "ep what ever it is ask DoDo"
        return self._ep

    @ep.setter 
    def ep(self, value):
        if type(value) == int:
            self._ep = value

        else:
            raise Exception("Error ep has to be type int")

    
    @property 
    def playertyp(self):
        "1 = soldier, 2 = robber, 3 = wizard "
        if self._wd == 1:
            return "soldier"
        elif self._wd == 2:
            return "robber"
        elif self._wd == 3:
            return "wizard"
        else:
            return "not defined"

    @playertyp.setter 
    def playertyp(self, value):
        if type(value) == str:
            if value == "soldier":
                self._playertyp = 1
            elif value == "robber":
                self._playertyp = 2
            elif value == "wizard":
                self._playertyp = 3
            else:
                self._playertyp = 0
        else:
            raise Exception("Error playertype has to be type str >> 1 = soldier, 2 = robber, 3 = wizard ")

def main():
    Phelper = PlayerHelper()

    testPlayer = Phelper.get_new_Wizard()
    testPlayer.name = "Oerb"
    testPlayer2 = Phelper.get_new_Soldier()
    testPlayer2.name = "DoDo"
    # print testPlayer.playertyp, testPlayer.playerId, testPlayer.name, testPlayer.hp, testPlayer.pp
    playerlist = Phelper.get_Playerlist()
    print "The Player UUID's are: " , playerlist.keys()
    print 2*"\n"
    for playerkey in playerlist.keys():
        print playerlist[playerkey].name, playerlist[playerkey].playertyp

if __name__ == "__main__":
    main()







