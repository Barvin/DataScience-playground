'''
Created on May 9, 2015

@author: arvinb
'''

from __builtin__ import file
from numpy import rate
file = open("crime_rates.csv", "r")
data = file.read()

rows = data.split("\n")

#remove scrap from the end
del rows[-1]

stats = []
for row in rows:
    split_row = row.split(",")
    split_row[1] = int(split_row[1])
    stats.append(split_row)

print(stats)

lowestCity = ""
lowestRate = stats[0][1]

for entry in stats:
    city = entry[0]
    rate = entry[1]
    
    if rate < lowestRate:
        lowestRate = rate
        lowestCity = city

print(lowestCity, " has the lowest crime rate of ", lowestRate)
        
    