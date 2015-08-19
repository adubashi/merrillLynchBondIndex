# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 15:19:44 2015

@author: aduba_000
"""

import Quandl
import json
from pprint import pprint
import Database
import databaseData


merril = databaseData.databaseData("PWSvEbf4_oUssZ3WqynR", "ML")
merril.getDailyData()
#merril.printCodes()
merril.printData()