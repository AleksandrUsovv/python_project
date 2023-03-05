import pandas as pd
df = pd.read_csv('test.csv', header=None, names=['Name', 'DOB', 'City'], nrows=5)
df.to_csv('testcopy.csv')