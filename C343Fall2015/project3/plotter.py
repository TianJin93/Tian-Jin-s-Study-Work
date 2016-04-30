import csv
import matplotlib.pyplot as plt
import math

xvals = []
yvals = []

with open('BST_times.csv', 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        xvals.append(row[0])
        yvals.append(row[1])

 
yvals_old = []

with open('AVL_times.csv', 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        yvals_old.append(row[1])

# plot the times
plt.xlabel('Segmentations'); plt.ylabel('Time')
xpts = [math.sqrt(float(xval)) for xval in xvals]
# plt.xticks(xpts, [str(sz) for sz in xpts])
plt.plot(xvals, yvals, 'bo-')
plt.plot(xvals, yvals_old, 'ro-')
plt.show()
