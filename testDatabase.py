# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 14:42:18 2015

@author: aduba_000
"""

import Quandl
import json
from pprint import pprint
import Database

#merril = merrilLynch.Bond("PWSvEbf4_oUssZ3WqynR")
merril = Database.Database("PWSvEbf4_oUssZ3WqynR", "ML")
merril.printCodes()
