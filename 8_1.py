import numpy as np

filename = "input.txt"

data_collected = np.loadtxt(filename)

print("{:.2f}".format(np.median(data_collected))
      ,"{:.2f}".format(np.mean(data_collected))
      ,"{:.2f}".format(np.std(data_collected)))