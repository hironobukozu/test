import numpy as np
import pandas as pd

inputs = []

print('INPUT PAIRS')
boo = True
number = 0
while boo == True:
    a = input()
    try:
        number = int(a)
        boo = False
    except ValueError:
        inputs.append(a)

df = pd.DataFrame(columns=['int','str'])

for i in range(len(inputs)):
    if number % int(inputs[i].split(":",1)[0]) == 0:
        tmp = pd.DataFrame([[int(inputs[i].split(":",1)[0]),inputs[i].split(":",1)[1]]],columns=['int','str'])
        df = pd.concat([df,tmp],axis=0)

df = df.sort_values(by=['int'])

if len(df) == 0:
    print(number)
else:
    answer = ""
    for i in range(len(df)):
        answer = answer + df.iloc[i,1]
    print(answer)

    
