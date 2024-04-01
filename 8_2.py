import numpy as np

def maxnum(num1,num2,num3):
     if max(num1,num2,num3) == num1: return 1
     elif max(num1,num2,num3) == num2: return 2
     elif max(num1,num2,num3) == num3: return 3

filename = "input.csv"
num1 ,num2, num3 = 0,0,0


data_collected = np.loadtxt(filename, delimiter= ',')

for i in range(data_collected.shape[0]): #做三次
     num1 += int(data_collected[i][0])
     num2 += int(data_collected[i][1])
     num3 += int(data_collected[i][2])
print(maxnum(num1,num2,num3))