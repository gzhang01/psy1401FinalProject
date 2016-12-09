import matplotlib.pyplot as plt
import numpy as np

# Adolescent data
# data = [0.7341336128818208, 0.16447534926933766, -0.2417122047543199, -0.6797294338392682, 0.7724816948607115, 0.27540472015067696, -0.3053749090269493, -0.7587147763693144]

# Adult data
# data = [0.7543738856796064, -0.7516291492682168, 0.08037633134235264, -0.09184234409150147, 0.23212215928453128, -0.2702666314146781, 0.25465070322601946, -0.2525798681383582]

# Adult data @ Iteration 1000
# data = [0.37030979069021086, -0.11047416154159734, 0.0012820966911621383, -0.1839287813239256, 0.37418710833876956, -0.002221990663824268, 0.026615896365241025, -0.37907934520621794]

row = 1000

allData = []
with open("data/adultQ.csv", "r") as f:
	allData = f.readlines()
data = allData[row].strip().replace("[", "").replace("]", "").split(", ")
data = data[4:] + data[:4]
data = [float(d) for d in data]


objects = ('G75P', 'G25P', 'L25P', 'L75P', 'G75C', 'G25C', 'L25C', 'L75C')
y_pos = np.arange(len(objects))
 
plt.bar(y_pos, data, align='center', alpha=0.5)
plt.ylim([-1, 1])
plt.xticks(y_pos, objects)
plt.ylabel('Q-value')
plt.axhline(0, color='black')
plt.title('Adult Q-Values @ Iteration ' + str(row))
plt.savefig("data/adultBar" + str(row) + ".png")
# plt.title('Adult Final Q-Values')
# plt.savefig("data/adultBar.png")
plt.show()