import random

class World:
	def __init__(self):
		self.choices = [(0, 1), (2, 3), (4, 5), (6, 7)]

	def get_train_choice(self):
		return self.choices[random.randint(0, len(self.choices) - 1)]

	def is_correct(self, choice, chance=0.75, rewardG=1, rewardL=-1):
		r1 = random.random()
		r2 = random.random()

		# Reward Complete
		if choice == 0:
			return (rewardG if r1 < chance else rewardG - 1, rewardG if r2 < 1 - chance else rewardG - 1)
		elif choice == 1:
			return (rewardG if r1 < 1 - chance else rewardG - 1, rewardG if r2 < chance else rewardG - 1)
		
		# Punishment Complete
		elif choice == 2:
			return (rewardL if r1 < 1 - chance else rewardL + 1, rewardL if r2 < chance else rewardL + 1)
		elif choice == 3:
			return (rewardL if r1 < chance else rewardL + 1, rewardL if r2 < 1 - chance else rewardL + 1)
		
		# Reward Partial
		elif choice == 4:
			return (rewardG if r1 < chance else rewardG - 1, None)
		elif choice == 5:
			return (rewardG if r1 < 1 - chance else rewardG - 1, None)

		# Punishment Partial
		elif choice == 6:
			return (rewardL if r1 < 1 - chance else rewardL + 1, None)
		elif choice == 7:
			return (rewardL if r1 < chance else rewardL + 1, None)

		else:
			raise Exception("Choice not valid!")

if __name__ == '__main__':
	world = World()
	samples = [[0, 0] for _ in xrange(8)]
	for i in xrange(8000):
		choices = world.get_train_choice()
		selection = choices[random.randint(0, len(choices) - 1)]
		rewards = world.is_correct(selection)
		samples[selection][0] += rewards[0]
		samples[selection][1] += 1
		if rewards[1] != None:
			other = selection + 1 if selection == choices[0] else selection - 1
			samples[other][0] += rewards[1]
			samples[other][1] += 1
	for s in samples:
		print "{0:2f}".format(100.0 * s[0] / s[1])




