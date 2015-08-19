# -*- coding: utf-8 -*-
import Quandl
import json
from pprint import pprint
import Database
import databaseData
import collections
"""
    jQuery Example
    ~~~~~~~~~~~~~~

    A simple application that shows how Flask and jQuery get along.

    :copyright: (c) 2015 by Armin Ronacher.
    :license: BSD, see LICENSE for more details.
"""
from flask import Flask, render_template

app = Flask(__name__)
'''
Time to refresh: 1 minute 20 seconds 
'''

myDict = {"Emerging Markets Corporate Bond Index OAS":"0",
          "Emerging Markets Corporate Bond Total Return Index":"0",
          "Emerging Markets High Grade Corporate Bond Index Yield":"0",
          "Euro Emerging Markets Corporate Bond Index (Yield)":"0",
          "Europe/Middle East/Africa (EMEA) Corporate Bond Total Return Index":"0",
          "IG Emerging Markets Corporate Bond Total Return Index":"0",
          "US AA Bond Index Yield":"0",
          "US AA Rated Total Return Index":"0",
          "US AAA Corporate Bond Total Return Index":"0",
          "US AAA rated Bond Index (yield)":"0",
          "US B Corporate Bond Total Return Index":"0",
          "US B rated Corporate Bond Index (yield)":"0",
          "US BB Bond Total Return Index":"0",
          "US BBB Bond Index (yield)":"0",
          "US CCC Bond Total Return Index":"0",
          "US CCC-rated Bond Index Yield":"0",
          "US Corporate BBB Total Return Index":"0",
          "US Corporate Bond A Total Return Index":"0",
          "US Corporate Bond A rated Index (yield)":"0",
          "US Corporate Bond Index Yield":"0",
          "US Corporate Bonds Total Return Index":"0",
          "US High Yield BB Corporate Bond Index Yield":"0",
          "US High Yield Corporate Bond Index (Yield)":"0",
          "US High Yield Corporate Bond Index OAS":"0"
         }


def getSortedDict(mydict):
    d = collections.OrderedDict()
    for key in sorted(mydict.iterkeys()):
        d[key] = mydict[key]
    return d

@app.route('/')
def intro():
    result = getSortedDict(myDict)
    return render_template('example.html', result=result)

@app.route('/data')
def hello_world():
    merril = databaseData.databaseData("PWSvEbf4_oUssZ3WqynR", "ML")
    merril.getDailyData()
    myDict = merril.dailyData
    result = getSortedDict(myDict)
    return render_template('example.html',result=result)



if __name__ == '__main__':
    app.run()
