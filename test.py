import numpy as np
import pandas as pd

inputs = []

f= open("input.txt","r")
line = f.readline()
number = 0
while line:
    try:
        number = int(line)
    except ValueError:
        inputs.append(line)
    line = f.readline()


df = pd.DataFrame(columns=['int','str'])
for i in range(len(inputs)):
    if number % int(inputs[i].split(":",1)[0]) == 0:
        tmp = pd.DataFrame([[int(inputs[i].split(":",1)[0]),inputs[i].split(":",1)[1][:-1]]],columns=['int','str'])
        df = pd.concat([df,tmp],axis=0)

df = df.sort_values(by=['int'])

if len(df) == 0:
    print(number)
else:
    answer = ""
    for i in range(len(df)):
        answer = answer + df.iloc[i,1]
    print(answer)

    
