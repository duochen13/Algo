import matplotlib.pyplot as plt
import collections


xx = []
yy = collections.defaultdict(list)

with open('./result.txt') as f:
	for line in f:
		line = line.rstrip('\n').split()
		k, time = line[0], line[1]
		if k == '=>':
			xx.append(int(line[-1]))
		elif k == 'Go':
			if time[-2:] != 'ms': # us
				time = float(time[:-2]) / 1000.0
				yy[k].append(time)
			else:
 				time = float(time[:-2])
 				yy[k].append(time)
		elif k == 'java':
			yy[k].append(float(time) / 1000000.0)
		else:
			yy[k].append(float(time))

for lang, vlist in yy.items():
	if lang == 'py':
		continue
	plt.plot(xx, vlist, label=lang)
plt.legend()
plt.ylabel("Time(ms)")
plt.xlabel("N for fibonacci")
plt.show()

