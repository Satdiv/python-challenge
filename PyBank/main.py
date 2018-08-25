#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 24 16:57:33 2018

@author: divya
"""
import os
import csv

PyBank_csv = os.path.join("./Resources" , "budget_data.csv")



with open(PyBank_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")


#with open('budget_data_1.csv') as csvfile:
#readCSV = csv.reader(csvfile, delimiter=',')
    total_Months = 0
    profit_loss = 0
    
    currentPL = 0
    previousPL = 0
    diffPL = 0
    avgChange = 0
    
    AvgPL = []
    greates_inc=["",0]
    greates_dec=["",99999999999]

    for row in csvreader:
        total_Months = total_Months+1
        if total_Months > 1 :
            profit_loss = profit_loss + int(row[1])
            previousPL = currentPL
            currentPL = int(row[1])
            if total_Months > 2 :
                diffPL = (currentPL - previousPL)
                # previousPL= #+ diffPL
                AvgPL.append(diffPL)
                if (diffPL > greates_inc[1]):
                    greates_inc[0]=row[0]
                    greates_inc[1]=diffPL
                if (diffPL < greates_dec[1]):
                    greates_dec[0]=row[0]
                    greates_dec[1]=diffPL
                print(AvgPL)
                print(greates_inc[0])
                         
avgChange = sum(AvgPL)/len(AvgPL)  #diffPL/(total_Months-2)
avgChange = round(avgChange,2)

print(AvgPL)

print('The total number of months included in the dataset: ' + str(total_Months-1))
print('The total net amount of "Profit/Losses" over the entire period: $' + str(profit_loss ))
print('The average change in "Profit/Losses" between months over the entire period :' +str(avgChange))


# print('The greatest increase in profits (date and amount) over the entire period :' )))
# print('The greatest decrease in losses (date and amount) over the entire period :'+ str(min(AvgPL)))
print("Greatest increse in"+str(greates_inc[0])+ "with value" +str(greates_inc[1]))
#print("Greatest increse in"+str(greates_inc[0])+"with value"+str(greates_inc[1]))
print("Greatest decrease in "+"(" +str(greates_dec[0])+")"+"  with value "+str(greates_dec[1]))