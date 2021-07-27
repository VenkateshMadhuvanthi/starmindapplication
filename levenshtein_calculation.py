#Header files
import os
import glob
import pandas as pd
#calculation of distance , reference: https://blog.finxter.com/how-to-calculate-the-levenshtein-distance-in-python/
def levenshtein(a, b):
    if not a: return len(b)
    if not b: return len(a)
    return min(levenshtein(a[1:], b[1:])+(a[0] != b[0]),
               levenshtein(a[1:], b)+1,
               levenshtein(a, b[1:])+1)
# retrieving the file as dataframe from url
sample = pd.read_csv('https://data.stadt-zuerich.ch/dataset/sid_stapo_hundenamen/download/20210103_hundenamen.csv')
#ignoring the unknown values 
new_sample= sample[sample.HUNDENAME!= 'unbekannt']
#printing the names 
for name in new_sample.HUNDENAME:
     if levenshtein("Luca",name) == 1:
        print(name)
