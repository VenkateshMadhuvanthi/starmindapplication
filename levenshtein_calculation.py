#Header files
import os
import glob
import pandas as pd
def levenshtein(a, b):
    if not a: return len(b)
    if not b: return len(a)
    return min(levenshtein(a[1:], b[1:])+(a[0] != b[0]),
               levenshtein(a[1:], b)+1,
               levenshtein(a, b[1:])+1)
sample = pd.read_csv('https://data.stadt-zuerich.ch/dataset/sid_stapo_hundenamen/download/20210103_hundenamen.csv')
new_sample= sample[sample.HUNDENAME!= 'unbekannt']
for name in new_sample.HUNDENAME:
     if levenshtein("luca",name) == 1:
        print(name)
