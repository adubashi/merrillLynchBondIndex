# -*- coding: utf-8 -*-
import Quandl
from pprint import pprint
import Database
import databaseData
import collections
import data
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
Time to refresh: 45 seconds 
'''

def getSortedDict(mydict):
    d = collections.OrderedDict()
    for key in sorted(mydict.iterkeys()):
        d[key] = mydict[key]
    return d

@app.route('/')
def intro():
    result = getSortedDict(data.myDict)
    result2 = result
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

