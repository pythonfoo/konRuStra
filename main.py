import os
import time
import random
import sys
import datetime
import math

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
		
class main(object):
	def giveEP(self,player,ep):
		player['ep'] += ep
		return player
	def giveMoney(self,player,gold):
		player['money'] = gold 
		return player
	def __init__(self):
		os.system('clear')
		self.figures = {}
	def randomCube(self,numOfCube,sizeOfCube):	
		result = []
		for i in range(numOfCube):
			result.append(random.randint(1,sizeOfCube))
		i = 0
		res = 0
		for i in range(len(result)):
			res += result[i]
		return res
	def printDict(self,dic):
		for key in dic:
			print key , dic[key]
	def printList(self,array):
		for i in range(len(array)):
			print array[i]
	def newWorld(self):
		world = {}
		counter = 1
		for i in range(1,11):
			for ii in range(1,11):
				world[counter] = {'x':ii,'y':i,'occ':False,'occFig':None,'threatened':False,'aff':False}
				# x: X-coordinate
				# y: Y-coordinate
				# occ: Is this field occupied?
				# occFig: Which kind of figure stand on this field?
				# threatened: Is this field threatened by a figure?
				counter += 1
		return world
	def defaultWorld(self):
		world = self.newWorld()
		world = self.setFigureOnWorld(world,'soldier',5,8,False)
		world = self.setFigureOnWorld(world,'soldier',4,9,False)
		world = self.setFigureOnWorld(world,'soldier',6,9,False)
		world = self.setFigureOnWorld(world,'robber',5,9,False)
		world = self.setFigureOnWorld(world,'wizard',5,10,False)
		return world	
	def compareTwoWorlds(self,worldOld,worldNew):
			difrences = []
			result = {'NOD':0,'Dif':difrences}
			for key in worldOld:
				if worldOld[key] != worldNew[key]:
					result['Dif'].append(worldNew[key])
					result['NOD'] += 1
			return result
	def setFigureOnWorld(self,world,figureDemand,x,y,aff):
		for key in world:
			if world[key]['x'] == x and world[key]['y'] == y:
				world[key]['occ'] = True
				world[key]['occFig'] = figureDemand
				world[key]['aff'] = aff
				if self.figures[figureDemand]['WD'] == 1:
					# The surronding fields
					if key <= 99:
						world[key+1]['threatened'] = True
						if key <= 91:
							world[key+9]['threatened'] = True
							if key <= 90:
								world[key+10]['threatened'] = True
								if key <= 89:
									world[key+11]['threatened'] = True
					if key >= 1:
						world[key-1]['threatened'] = True
						if key >= 9:
							world[key-9]['threatened'] = True
							if key >= 10:	
								world[key-10]['threatened'] = True
								if key >= 11:
									world[key-11]['threatened'] = True
					# 8 fields are threatened
				if self.figures[figureDemand]['WD'] == 2:
					i = 0
					robTFields = (1,2,8,9,10,11,12,18,19,20,21,22)
					for i in range(len(robTFields)):
						if key <= (100-robTFields[i]):
							world[key+robTFields[i]]['threatened'] = True
					for i in range(len(robTFields)):
						if key >= (robTFields[i]):
							world[key-robTFields[i]]['threatened'] = True					
					
									
					# 24 fields are threatened
				if self.figures[figureDemand]['WD'] == 3:
					i = 0
					widTFields = (2,3,7,8,12,17,18,19,29,21,22,23,27,28,29,30,31,32,33)
					for i in range(len(widTFields)):
						if key <= (100-widTFields[i]):
							world[key+widTFields[i]]['threatened'] = True
					for i in range(len(widTFields)):
						if key <= (100-widTFields[i]):
							world[key+widTFields[i]]['threatened'] = True
					
		return world
	def newPlayer(self,name,ep,level,money,difficulty,numS,numR,numW):
		player = {}
		player['name'] = name
		player['level'] = level
		player['money'] = money
		player['difficulty'] = difficulty
		player['inv'] = {'s':numS,'r':numR,'w':numW}
		player['ep'] = ep
		return player
	def defaultPlayer(self):
		player = self.newPlayer('Human',1,1000,1,0,0,0)
		return player
	def newFig(self,name,hp,pp,wd,soa,hpReg,ppReg,price):
	# name = Name
	# hp = Healt Point
	# pp = Perseverance Point
	# wd = Weapon Distance
	# soa = Strength of arms
	# hpReg = Health Point Recharge
	# ppReg = Perseverance Point Recharge
	# price = Price
		self.figures[name] = {'HP':hp,'HPReg.':hpReg,'PP':pp,'PPReg.':ppReg,'WD':wd,'SoA':soa,'Price':price}
	def defaultFigures(self,figures):
		figures['soldier'] = {'HP':1250,'PP':250,'WD':1,'SoA':50,'HPReg':3,'PPReg':1,'Price':500}
		figures['robber'] = {'HP':750,'PP':750,'WD':2,'SoA':45,'HPReg':2,'PPReg':2,'Price':500}
		figures['wizard'] = {'HP':1000,'PP':500,'WD':3,'SoA':40,'HPReg':1,'PPReg':3,'Price':500}
		return figures
		# self.printDict(self.figures)
	def experienceGen(self):
		EPperLvl = []
		ep = 1
		for i in range(21):
			EPperLvl.append(pow(2,i))
		return EPperLvl
	def levelTest(self,expSteps,ep,level):
		for i in range(len(expSteps)):
			if ep >= expSteps[i]:
				level = i + 1
		return level
	def trade(self,figures,money,purchase_demand,tmpInv):
		inv = {'s':tmpInv['s'],'w':tmpInv['w'],'r':tmpInv['r']}
		gold = money
		if purchase_demand == 's':	
			gold -= figures['soldier']['Price']
			inv['s'] += 1
		elif purchase_demand == 'w':
			gold -= figures['wizard']['Price']
			inv['w'] += 1
		elif purchase_demand == 'r':
			gold -= figures['robber']['Price']
			inv['r'] += 1
		return {'money':gold,'inv':inv}

testC = test()
player = testC.player
enemy = testC.mainC.newPlayer('enemy',20134,1,1000000,1,0,0,0)
# print testC.mainC.printDict(testC.autoRandomFillInventory(50,player))
enemy = testC.autoRandomFillInventory(50,enemy)
enemy = testC.testGiveEP(enemy,100,10000)
print testC.mainC.printDict(testC.testLevelTest(enemy))
