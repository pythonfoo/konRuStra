#!/usr/bin/env python 
#-*- coding: utf-8 -*-
""" Game objects for konRuStra """
__author__ = "oerb"
__copyright__ = "GPL 2013"
__license__ = "GPL" 

__all__ = ["PlayerHelper"]

import uuid # UniceIdentify Objects

class FiguresHelper(object):
    "gives Methods to get default Figures and other Figuremanipulations"
    def __init__(self):
        self._figurelist = {}

    def _figure_add(self, figurevalue):
        "add Player to Playerlist"
        if isinstance(figurevalue,Figure):
            self._figurelist[figurevalue.figureId] = figurevalue
        else:
            raise Exception("Error type Player hast to be instance of Player Object")
    
    def figure_remove(self, figurevalue): 
        "removes Player from Playerlist"
        if isinstance(figurevalue, Figure):
            self._figurelist.pop(figurevalue.figureId, None)
        else:
            raise Exception("Error type Player hast to be instance Player Object")

    def get_Figurelist(self):
        "returns intern Playerlist - must be replaced by inteligent Methods"
        #TODO: nomore return of intern Playerlist just uses Methods to manipulate
        return self._figurelist

    def get_new_Soldier(self):
        "returns a new Soldier with defaults and adds to Playerlist"
        soldier = gamer()
        soldier.hp = 1250
        soldier.pp = 250
        soldier.wd = 1
        soldier.soa = 50
        soldier.hpReg = 3
        soldier.ppReg = 1
        soldier.price = 500
        soldier.figuretyp = "soldier"
        self._figure_add(soldier)
        return soldier

    def get_new_Robber(self):
        "returns a new Robber with defaults and adds to Playerlist"
        robber = gamer()
        robber.hp = 750
        robber.pp = 750 
        robber.wd = 2
        robber.soa = 45
        robber.hpReg = 2
        robber.ppReg = 2
        robber.price = 500
        robber.figuretyp = "robber"
        self._figure_add(robber)
        return robber

    def get_new_Wizard(self):
        "returns a new Wizard with defaults and adds to Playerlist"
        wizard = gamer()
        wizard.hp = 1000
        wizard.pp = 500
        wizard.wd = 3
        wizard.soa = 40
        wizard.hpReg = 1
        wizard.ppReg = 3
        wizard.price = 500
        wizard.figuretyp = "wizard"
        self._figure_add(wizard)
        return wizard

class Figure(object):
    """ Dataclass for every Figure to store and give data to every Figure"""
    def __init__(self):

        self._figureId = uuid.uuid4()
        self._name = ""

    @property 
    def figureId(self): 
        " Returns the Figure UUID"    
        return self._figureId 

    @property 
    def name(self): 
            return self._name 

    @name.setter 
    def name(self, value):
        if type(value) == str:
            self._name = value
        else:
            raise Exception("Error Figurename has to be Type Str")

class Bot(Figure):
    """ Used for Bots in the AI """
    pass

class gamer(Figure):
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
        self._figuretyp = 0 # 1 = soldier, 2 = robber, 3 = wizard 
    

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
    def figuretyp(self):
        "1 = soldier, 2 = robber, 3 = wizard "
        if self._figuretyp == 1:
            return "soldier"
        elif self._figuretyp == 2:
            return "robber"
        elif self._figuretyp == 3:
            return "wizard"
        else:
            return "not defined"

    @figuretyp.setter 
    def figuretyp(self, value):
        if type(value) == str:
            if value == "soldier":
                self._figuretyp = 1
            elif value == "robber":
                self._figuretyp = 2
            elif value == "wizard":
                self._figuretyp = 3
            else:
                self._figuretyp = 0
        else:
            raise Exception("Error figuretype has to be type str >> 1 = soldier, 2 = robber, 3 = wizard ")

def main():
    Fhelper = FiguresHelper()

    testFigure = Fhelper.get_new_Wizard()
    testFigure.name = "Oerb"
    testFigure2 = Fhelper.get_new_Soldier()
    testFigure2.name = "DoDo"
    # print testPlayer.playertyp, testPlayer.playerId, testPlayer.name, testPlayer.hp, testPlayer.pp
    figurelist = Fhelper.get_Figurelist()
    print "The Player UUID's are: " , figurelist.keys()
    print 2*"\n"
    for figurekey in figurelist.keys():
        print figurelist[figurekey].name, figurelist[figurekey].figuretyp

if __name__ == "__main__":
    main()







