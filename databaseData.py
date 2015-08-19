# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 15:15:22 2015

@author: aduba_000
"""
import Quandl
from pprint import pprint
import Database

class databaseData:
    def __init__(self, key, datasource):
        self.database = Database.Database(key,datasource)
        self.dailyData = {}
    
    def printCodes(self):
        for i in self.database.dataCodes:
            print i
            print self.database.dataCodes[i] 
    
    def getDailyData(self):
        for i in self.database.dataCodes:
            test = Quandl.get(i, authtoken=self.database.getKey())
            self.dailyData[self.database.dataCodes[i]] = self.getMostRecentData(test)
    
    def getMostRecentData(self,data):
        m = data.iloc[data.size - 1]
        return float(m[0])
    
    def printData(self):
        pprint(self.dailyData)
        
    