__author__ = 'anne'

from numpy import genfromtxt
import numpy as np
import matplotlib.pyplot as plt
Distance = []
Tie = []

data = genfromtxt('D:\\Class of MSc Informatic at TUM\\IDP\Code\\IDP_text_miner\\distance_tie_strength_list_clean.csv', delimiter=',')

for row in data:
    Distance.append(row[0])
    Tie.append(row[1])

Tie = np.array(Tie)
Distance = np.array(Distance)

threshold = Tie.mean()
max = np.max(Distance)
min = np.min(Distance)
# df = pd.read_csv('D:\\Class of MSc Informatic at TUM\\IDP\Code\\IDP_text_miner\\distance_tie_strength_list_clean.csv', sep=',',header=None)
bins = np.linspace(-1, max+1, 100)
freq, bins = np.histogram(Distance, bins)
plt.hist(Distance, bins)
plt.title("Distance Histogram")
plt.xlabel("Value")
plt.ylabel("Frequency")


d = np.digitize(Distance, bins)

friends_freq = np.zeros(100)

print d[0]
for i in xrange(len(d)):
    if Tie[d[i]] > threshold:
        friends_freq[d[i]] += 1

for i in xrange(len(friends_freq)):
    friends_freq[i] = friends_freq[i]/freq[i]
    print "Probability of bucket ", i, " is: ", friends_freq[i]
plt.show()
