import numpy as np

filename = "input.csv"
filename2 = "output.csv"

data = np.loadtxt(filename,delimiter=',')

for i in range(data.shape[0]): #执行5次
    if(i % 2 == 0): #奇数行,偶数列
        for j in range(1,len(data[i]),2):
            data[i][j] /= 2
    else: #偶数行,奇数列
        for j in range(0, len(data[i]),2):
            data[i][j] /= 2

np.savetxt(filename2,data,delimiter=',',fmt = '%g')  #保存CSV文件