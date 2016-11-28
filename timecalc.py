#!/usr/bin/env python

'''
Written by: Mike Hauss

This script accepts a whole number as a number of seconds and tells how many years, months, days, weeks, days, hours, minutes and seconds it is equal to.
If the argument is -m; -u; -d; -w and/or -y, tell how many seconds
'''
import pdb
import argparse

# Variables
yearSecs = 31536000
monthSecs = 2592000  # 30 day month
weekSecs = 604800
daySecs = 86400
hourSecs = 3600
minSecs = 60
years = ''
months = ''
weeks = ''
days = ''
hours = ''
mins = ''
seconds = ''
secsRemain = ''

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-s','--secs', action="store", help="Seconds; must be a positive whole number", type=int)
    parser.add_argument('-m','--mins', action="store", help="Minutes; must be a positive whole number", type=int)
    parser.add_argument('-u','--hours', action="store", help="hoUrs; must be a positive whole number", type=int)
    parser.add_argument('-d','--days', action="store", help="Days; must be a positive whole number", type=int)
    parser.add_argument('-w','--weeks', action="store", help="Weeks; must be a positive whole number", type=int)
    parser.add_argument('-o','--months', action="store", help="mOnths; must be a positive whole number", type=int)
    parser.add_argument('-y','--years', action="store", help="Year; must be a positive whole number", type=int)
    args = parser.parse_args()

def compare(u): 
    #pdb.set_trace()
    if u > yearSecs:
        calcYears(u)    # each of these is a list with remainder as [1]
    elif u > monthSecs:
        calcMonths(u)
    elif u > weekSecs:
        calcWeeks(u)
    elif u > daySecs:
        calcDays(u)
    elif u > hourSecs:
        calcHours(u)
    elif u >= minSecs:
        calcMins(u)
    else:
        seconds = u

def calcYears(s):
    values = divmod(s,yearSecs)     # returns a list
    numYears = values[0]            # whole number
    secsRemain = values[1]          # remainder
    # leap year, add a day
    if numYears > 3:
        secsRemain += 86400
    return [numYears, secsRemain]

#pdb.set_trace()
def calcMonths(s):
    values = divmod(s,monthSecs)
    numMonths = values[0]
    secsRemain = values[1]
    global months
    return [numMonths, secsRemain]

#pdb.set_trace()
def calcWeeks(s):
    values = divmod(s,weekSecs)
    numWeeks = values[0]
    secsRemain = values[1]
    global weeks
    return [numWeeks, secsRemain]

#pdb.set_trace()
def calcDays(s):
    values = divmod(s,daySecs)
    numDays = values[0]
    secsRemain = values[1]
    global days
    return [numDays, secsRemain]

#pdb.set_trace()
def calcHours(s):
    values = divmod(s,hourSecs)
    numHours = values[0]
    secsRemain = values[1]
    global hours
    return [numHours, secsRemain]

#pdb.set_trace()
def calcMins(s):
    values = divmod(s,minSecs)
    numMins = values[0]
    secsRemain = values[1]
    global mins
    if secsRemain > 0:
        return [numMins, secsRemain]
    else:
        return numMins

if __name__ == '__main__':
    main()
