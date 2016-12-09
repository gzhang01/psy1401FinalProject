import math
import random
from world import World

class Person:
	def __init__(self, world, a1=0.3, a2=0.3, a3=0.3, rewardG=1, rewardL=-1, chance=0.75, file=None, beta=5, q=None, v=None):
		self.a1 = a1
		self.a2 = a2
		self.a3 = a3
		self.beta = beta
		self.q = [[0 for _ in xrange(2)] for _ in xrange(4)] if q == None else q
		self.v = [0 for _ in xrange(4)] if v == None else v
		self.world = world
		self.file = file
		self.rewardG = rewardG
		self.rewardL = rewardL
		self.chance = chance

		if self.file:
			with open(self.file, 'w') as f:
				pass

	def makeChoice(self, choices, state):
		prob_first = 1.0 / (1 + math.e ** (self.beta * (self.q[state][1] - self.q[state][0])))
		return (1, 0) if random.random() > prob_first else (0, 1)

	def train(self):
		# Get and make choice
		choices = self.world.get_train_choice()
		state = choices[0] / 2
		c, u = self.makeChoice(choices, state)
		
		# Get rewards & total reward
		r_c, r_u = self.world.is_correct(choices[c], self.chance, self.rewardG, self.rewardL)
		r_u = r_u if r_u != None else self.q[state][u]
		r_tot = (r_c + r_u) / 2.0

		# Update state value
		d_v = r_tot - self.v[state]
		self.v[state] = self.v[state] + self.a3 * d_v

		# Update Q value
		d_c = r_c - self.v[state] - self.q[state][c]
		d_u = r_u - self.v[state] - self.q[state][u]
		self.q[state][c] = self.q[state][c] + self.a1 * d_c
		self.q[state][u] = self.q[state][u] + self.a1 * d_u

		# print choices, (c, u), (r_c, r_u)
		# print self.v
		# print self.q
		# raw_input()

		if self.file:
			with open(self.file, 'a') as f:
				f.write(str(self.q) + "\n")

		return choices, (c, u)


if __name__ == '__main__':
	w = World()
	adult = Person(w, 0.005, 0.0, 0.0, 1, -1, 0.75, "data/adolescentQPrison.csv")
	# adolescent = Person(w, 0.005, 0, 0, "data/adolescentQ.csv")
	for _ in xrange(800):
		adult.train()
		# adolescent.train()
	adult.chance = 0.75
	adult.rewardG = -2
	adult.rewardL = -4
	for _ in xrange(200):
		adult.train()
	adult.chance = 0.75
	adult.rewardG = 1
	adult.rewardL = -1
	for _ in xrange(9000):
		adult.train()
	for arr in adult.q: print arr, arr[0] - arr[1]
	# for arr in adolescent.q: print arr, arr[0] - arr[1]

