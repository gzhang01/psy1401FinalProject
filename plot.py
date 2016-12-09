import matplotlib.pyplot as plt

file = "adolescentQPrison"
# file = "adultQRehab"
# file = "adultQ"
infile = "data/" + file + ".csv"
outfile = "data/" + file

data = [[] for _ in xrange(8)]

with open(infile, 'r') as f:
	for line in f:
		line = line.strip().replace("[", "").replace("]", "").split(", ")
		for i in xrange(len(line)):
			data[i].append(line[i])

# Uncomment this part to show progression of plots
#	1. G75 Complete
# 	2. G25 Complete
#	3. L25 Complete
# 	4. L75 Complete	
#	5. G75 Partial
# 	6. G25 Partial
#	7. L25 Partial
# 	8. L75 Partial

# #### Adult Data
# for i in xrange(1, len(data) + 1):
# 	for j in xrange(i):
# 		plt.plot(data[j])
# 		if j ==  0: plt.text(10100, 0.18, "G75C")
# 		if j ==  1: plt.text(10100, -0.32, "G25C")
# 		if j ==  2: plt.text(10100, 0.25, "L25C")
# 		if j ==  3: plt.text(10100, -0.25, "L75C")
# 		if j ==  4: plt.text(10100, 0.73, "G75P")
# 		if j ==  5: plt.text(10100, -0.77, "G25P")
# 		if j ==  6: plt.text(10100, 0.07, "L25P")
# 		if j ==  7: plt.text(10100, -0.12, "L75P")
# 	plt.suptitle('Adult Q Values', fontsize=20)
# 	plt.axis([0, 10000, -0.85, 0.85])
# 	plt.savefig(outfile + str(i) + ".png")
# 	plt.show()

# # Uncomment this part to draw and save final plot

##### Adult Data
for i in xrange(len(data)):
	plt.plot(data[i])
# plt.text(10100, 0.18, "G75C")
# plt.text(10100, -0.32, "G25C")
# plt.text(10100, 0.25, "L25C")
# plt.text(10100, -0.25, "L75C")
# plt.text(10100, 0.73, "G75P")
# plt.text(10100, -0.77, "G25P")
# plt.text(10100, 0.07, "L25P")
# plt.text(10100, -0.12, "L75P")
plt.suptitle('Adolescent Q Values (Prison)', fontsize=20)
plt.axis([0, 10000, -0.85, 0.85])
plt.savefig(outfile + ".png")
plt.show()



# ### Adolescent Data
# for i in xrange(1, len(data) + 1):
# 	for j in xrange(i):
# 		plt.plot(data[j])
# 		if j ==  0: plt.text(10100, 0.77, "G75C")
# 		if j ==  1: plt.text(10100, 0.26, "G25C")
# 		if j ==  2: plt.text(10100, -0.34, "L25C")
# 		if j ==  3: plt.text(10100, -0.78, "L75C")
# 		if j ==  4: plt.text(10100, 0.7, "G75P")
# 		if j ==  5: plt.text(10100, 0.14, "G25P")
# 		if j ==  6: plt.text(10100, -0.26, "L25P")
# 		if j ==  7: plt.text(10100, -0.7, "L75P")
# 	plt.suptitle('Adolescent Q Values', fontsize=20)
# 	plt.axis([0, 10000, -0.85, 0.85])
# 	plt.savefig(outfile + str(i) + ".png")
# 	plt.show()


# ### Adolescent Data
# for i in xrange(len(data)):
# 	plt.plot(data[i])
# plt.text(10100, 0.77, "G75C")
# plt.text(10100, 0.26, "G25C")
# plt.text(10100, -0.34, "L25C")
# plt.text(10100, -0.78, "L75C")
# plt.text(10100, 0.7, "G75P")
# plt.text(10100, 0.14, "G25P")
# plt.text(10100, -0.26, "L25P")
# plt.text(10100, -0.7, "L75P")
# plt.suptitle('Adolescent Q Values', fontsize=20)
# plt.axis([0, 10000, -0.85, 0.85])
# plt.savefig(outfile + ".png")
# plt.show()
