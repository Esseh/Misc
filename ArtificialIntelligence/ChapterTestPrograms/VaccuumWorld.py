import random as r

def select(list): return

class World:
	def __init__(self):
		x = lambda(list):list[r.randint(0,1)]
		self.rooms = {"left":x(["dirty","clean"]),"right":x(["dirty","clean"])}
		self.location = x(["left","right"])
		self.perceptSequence = []
	def percept(self):
		self.perceptSequence += [(self.location,self.rooms[self.location])]
		return (self.location,self.rooms[self.location])
	def act(self):
		self.rooms[self.location], self.location = {
			("left","clean") : ("clean","right"),
			("left","dirty") : ("clean","left"),
			("right","clean"): ("clean","left"),
			("right","dirty"): ("clean","right"),
		}[self.percept()]
	def unclean(self):
		for i in self.rooms:
			if self.rooms[i] == "dirty": return True
		return False


def Main():
	worldIs = World()
	while worldIs.unclean():
		print (worldIs.location,worldIs.rooms[worldIs.location])
		worldIs.act()
	print worldIs.perceptSequence