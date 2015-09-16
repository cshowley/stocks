import csv
import numpy
import os
import random

master={}

#Build master dict

for filename in os.listdir('/Users/Red/Stocks/2012_2015'):
    if filename != '.DS_Store':
        prices=[]
        with open ('/Users/Red/Stocks/2012_2015/{0}'.format(filename), 'rU') as file: 
            data = csv.reader(file,delimiter=',')
            for line in data:
                try:
                    prices.append(float(line[6]))
                except:
                    pass
            master[filename] = prices
    else:
        pass
  
#buying calculator

def daybreak (i, money):
    
    for key in master:
        print key
        candidates = []    
        
        today = master[key][(len(master[key])-31-i)]
            
        smathirty = numpy.mean(master[key][(len(master[key])-30-i):(len(master[key])-1-i)])
            
        smafive = numpy.mean(master[key][(len(master[key])-30-i):(len(master[key])-25-i)])

        if today/smathirty <= 0.98:
            candidates.append(key)
    
    if len(candidates) > 0:    
        selection = random.choice(candidates)
        price = master[selection][(len(master[key])-i)]
        shares = money / price
        own = True
        daybought = i
        return daybought,selection,shares


#selling follower

def salesman(daybought,selection,shares):
    for i in range(len(master[selection])):
        
        today = master[selection][(len(master[selection])-31-i-daybought)]
        smafive = numpy.mean(master[selection][(len(master[selection])-30-i):(len(master[selection])-25-i)])
        
        if today / smafive >= 1.02 and shares !=0 :
            money = today * shares
            daysold = i
            shares = 0
            return daysold, money
            
        elif shares == 0:
            pass


#running buying and selling

z = 1
money = 10000

while z < 100:
    a = daybreak(z, money)
    print a
    z += 1

