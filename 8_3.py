import numpy as np

def maxnum(num1, num2):
    if max(num1, num2) == num1:
        return 1
    elif max(num1, num2) == num2:
        return 2

filename = "input.csv"
data_collected = np.loadtxt(filename, delimiter= ',')

client1,client2 = 0,0

for i in range(data_collected.shape[0]):
    if -4 <= np.std(data_collected[i]) <= 4:  # np.std() 计算标准差
        client1 += 1
    else: client2 += 1

print(maxnum(client1,client2))