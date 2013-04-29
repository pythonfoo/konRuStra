#!/usr/bin/env python

from main import *

class test(object): # a class to test the main functions
	def __init__(self):
		self.mainC = main()
		self.world = self.mainC.newWorld()
		self.player = self.mainC.newPlayer('test',0,1,1000000,1,0,0,0)
		self.figures = {}
		self.figures = self.mainC.defaultFigures(self.figures)
	def testTrade(self,player,figDemand):
		money = player['money']
		inv = player['inv']
		tradingProfit = self.mainC.trade(self.figures,money,figDemand,inv)
		player['money'] = tradingProfit['money']
		player['inv'] = tradingProfit['inv']
		return player
	def autoRandomFillInventory(self,length,player):
		for i in range(1,length+1):
			player = self.testTrade(player,random.choice(['w','s','r']))
		return player
	def testLevelTest(self,player):
		player['level'] = self.mainC.levelTest(self.mainC.experienceGen(),player['ep'],player['level'])
		return player
	def testGiveEP(self,player,epRangeMin,epRangeMax):
		player = self.mainC.giveEP(player,random.randint(epRangeMin,epRangeMax))
		return player
		
testC = test()
player = testC.player
enemy = testC.mainC.newPlayer('enemy',20134,1,1000000,1,0,0,0)
# print testC.mainC.printDict(testC.autoRandomFillInventory(50,player))
enemy = testC.autoRandomFillInventory(50,enemy)
enemy = testC.testGiveEP(enemy,100,10000)
print testC.mainC.printDict(testC.testLevelTest(enemy))
