import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('data.csv', encoding='gbk', header=None, sep='\t')
X = df.iloc[:,[i for i in range(3 , 33)]]
y = df.iloc[:, [2]]
print(X)
print(y)

