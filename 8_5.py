import numpy as np

filename = "input.csv"
filename2 = "output.csv"
myList = []

data = np.loadtxt(filename,delimiter = ',')
for i in range(len(data[0])): #列数次,30次
    for j in range(0,data.shape[0]): #行数次,15次循环
        myList.append(data[j][i])
    data[0][i] = int(1.5 * np.mean(myList))
    myList.clear()

np.savetxt(filename2,data,delimiter=',',fmt = '%g')  #保存CSV文件