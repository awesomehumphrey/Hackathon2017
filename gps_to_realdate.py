# -*- coding: utf-8 -*-
"""
Created on Sat Mar 18 13:57:36 2017

@author: Humphrey
"""
from astropy.time import Time
import pandas as pd

df = pd.read_csv('C:/Users/Humphrey/Desktop/11/Machine11.csv')

originTime = df['OriginationTime']
transTime = df['TransmissionTime']

originTime = Time(originTime, format='gps')
transTime =  Time(transTime, format='gps')

df['NewOriginTime'] = Time.to_datetime(originTime)
df['NewTransmissionTime'] = Time.to_datetime(transTime)

df.to_csv('C:/Users/Humphrey/Desktop/11/NewMachine11.csv')