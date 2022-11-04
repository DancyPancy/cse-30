from random import randint
import matplotlib.pyplot as plt

sums = []
trials = []

for i in range(100):
    roll1 = randint(1, 6)
    roll2 = randint(1, 6)
    sums.append(roll1 + roll2)
    trials.append(i)

fig = plt.figure(tight_layout=True)

graph = fig.add_subplot(2, 2, 1)
graph.scatter(trials, sums, s=5)

graph = fig.add_subplot(2, 2, 2)
graph.plot(trials, sums)

graph = fig.add_subplot(2, 2, 3)
graph.hist(sums, bins=11, range=(2, 12), )

sum_count = []
for i in range(2, 13):
    count = len([x for x in sums if x == i])
    print(count)
    sum_count.append(count)


graph = fig.add_subplot(2, 2, 4)
graph.pie(sum_count, labels=range(2, 13))

plt.show()
