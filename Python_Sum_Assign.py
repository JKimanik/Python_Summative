"""
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
Created on Sun Mar 17 12:16:23 2019
@author: James Kimani
Python Summative Assignment
"""
import random 
import datetime
import csv 

"""
Problem 1:
Generate a dummy dataset that you can use to prove your solutions work with.
ACCEPTANCE CRITERIA
i. The order of the objects must be sequential, ( ie. 1,2,3...32. ) since each 
  number references a different pipeline region.
ii. Your generated dataset needs to return a single set of data,
  that has 32 entries, with each entry returning 16 floats. 
ii. The 16 floats returned will be between 0 and 1
"""
def Datagenerator():
    print("SET:", count) #Show What count of data set you are on
    Clustereadings= []
    Sensor_Reading = []
    for Cluster in range(0,32):#32 clusters for sensors
        for sensors in range(0,16):#16 Sensors for each cluster
            Sensor_Reading.append(float('%.3f'%random.random())) #random float on each sensor
            Clustereadings.append(Sensor_Reading)           
            Sensor_Reading = []
    print(Clustereadings)
    return Clustereadings
    
  
"""
Problem 2:
Once you have your dataset to work with you will need to show that you can 
store this data with every iteration of the data set so no data is lost.
ACCEPTANCE CRITERIA
Every time your data set is generated the output should be stored and saved
For a challenge you could try to write the data to a file
New data should not overwrite historical data
For an extra challenge you can try to date and time stamp each interval of 
data collection

"""
def Writetofile(Completedata): #
        Storagefile = open("SensorDump.csv","a") #append to file
        Storagefile.write("Time stop: {}".format(datetime.datetime.now())) 
        Storagefile.write(str(Completedata)) #Write the data to the file, change to string 
        #print(Completedata)
        #print("Timestamp{}".format(datetime.datetime.now()))
"""
Problem 3:
Write a function that will test the incoming data for possible strings entries
ACCEPTANCE CRITERIA
Create a copy of a "corrupted" data set containing at least one entry where the value is "err"
Your function should check for this error
Convert the string to a numerical value that can be uniquely identified as the error
Create an error log that records that the error happened and which of the sensors the error occurred with
For a challenge you can try to date and time stamp the log entries
"""
def Corrupteddata(data): #generate errors randomly in the dataset
  errors = random.randrange(1)
  for i in range(errors):
    Sens_clust = random.randrange(1, 32, 1)
    sens_pos = random.randrange(1, 16, 1)
    data[Sens_clust][sens_pos] = 'err'
    
"""Main loop"""
count =1
while (count<=3): #Problem 2 generate diffrent datasets
    data ={}            
    Generatedata =[]
    datain = Datagenerator() #Sensor data gernerator       
    Writetofile(Generatedata)
    Corrupteddata(data)
    count=count+1 # count iterations         
