# CI SHI
# 2020/03/16
#Project 6

import numpy as np
import random
import pandas as pd
import statistics
random.seed(1000)
matrix = []
columname = []
for i in range(10):
    name2 = "col"+str(i)
    columname.append(name2)
print(columname)
for i in range(1000):
    tuple = []
    for j in range(10):
        ele = random.randint(0,1000)
        tuple.append(ele)
    matrix.append(tuple)
Matrix = np.array(matrix)
df = pd.DataFrame(Matrix)
df.columns = columname
df.to_csv('D:\python\pere\matrix.csv',index=False,header=True)
print(df)

number = int(input('please enter the number'))-1
col = list(zip(*matrix))
colchoose = col[number]
colshow = np.array(colchoose)
print(colchoose)
print(f'the mean of value in column {number} is {statistics.mean(colchoose)}')
print(f'the standard deviation of value in column {number} is {statistics.stdev(colchoose)}')
print(f'the mode of value in column {number} is {statistics.mode(colchoose)}')
print(f'the median of value in column {number} is {statistics.median(colchoose)}')


outfile= open('Summary','a')
contect = f'The column names used in the file: {columname}\n'\
          f'we choose the column {number}, i.e col{number+1} as the example for following statistic\n' \
          f'the col{number+1} is {colshow}\n'
contect +=f'the mean of value in column {number} is {statistics.mean(colchoose)}\n'\
          f'the mode of value in column {number} is {statistics.mode(colchoose)}\n'\
          f'the standard deviation of value in column {number} is {statistics.stdev(colchoose)}\n'\
          f'the median of value in column {number} is {statistics.median(colchoose)}'
outfile.write(contect)
outfile.close()
