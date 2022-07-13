# 
# create a list called result which contains the numbers that are common in both files.
# 

import pandas as pd

file1 = pd.read_csv("Projects/day-26-list-comp/e1-exercise/file1.txt", header=None, names=["Number1"])
file2 = pd.read_csv("Projects/day-26-list-comp/e1-exercise/file2.txt", header=None, names=["Number2"])

list_f1 = file1["Number1"].to_list()
list_f2 = file2["Number2"].to_list()

result = [i for i in list_f1 if i in list_f2]

print(result)