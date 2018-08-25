#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 25 17:37:07 2018

@author: divya
"""

import os
import csv

PyPoll_csv = os.path.join("./Resources" , "election_data.csv")

with open(PyPoll_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    

    totalVoters = 0
    candidate = {None}
   
    for row in csvreader:     
        totalVoters = totalVoters+1
        if totalVoters > 2:
            candidate.add(row[2])
#        print(row[2])
        
 

#print(candidate)        
            
            
            
print("The total number of votes cast :" + str(totalVoters-1))    
print("A complete list of candidates who received votes :" + str(candidate))   