# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 14:04:58 2015

@author: aduba_000
"""

import Quandl
from pprint import pprint


class Database:
    def __init__(self, key, datasource):
        self.key = key;
        self.datasource = datasource; 
        self.dataCodes = {};
        self.getDatasets()
        self.getListOfCodes()
    def getKey(self):
        return self.key;
    def getDatasource(self):
        return self.datasource;
    def getDatasets(self):
        print "In get datasets"
        datasets = Quandl.search(query = "", source = self.datasource, prints = False, authtoken=self.key)
        return datasets;
    def getListOfCodes(self):
        data = self.getDatasets()
        for i in data:
            code = i['code']
            name = i['name']
            #print code
            #print name
            self.dataCodes[code] = name
    def printCodes(self):
        pprint(self.dataCodes)
    
    
        
    


    

    



