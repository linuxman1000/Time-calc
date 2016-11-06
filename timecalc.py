#!/usr/bin/env python

'''
Written by: Mike Hauss

This script accepts a whole number as a number of seconds and tells how many years, months, days, weeks, days, hours, minutes and seconds it is equal to.
If the argument is -m; -u; -d; -w and/or -y, tell how many seconds
'''
import pdb
import argparse

# Variables
yearSecs = 31536000  # seconds per calendar year
monthSecs = 2592000  # 30 day month
weekSecs = 604800
daySecs = 86400
hourSecs = 3600
minSecs = 60
years = 0
months = 0
weeks = 0
days = 0
hours = 0
mins = 0
seconds = 0 
secsRemain = 0

parser = argparse.ArgumentParser()
parser.add_argument('-s','--secs', action="store", help="Seconds; must be a positive whole number", type=int)
parser.add_argument('-m','--mins', action="store", help="Minutes; must be a positive whole number", type=int)
parser.add_argument('-u','--hours', action="store", help="hoUrs; must be a positive whole number", type=int)
parser.add_argument('-d','--days', action="store", help="Days; must be a positive whole number", type=int)
parser.add_argument('-w','--weeks', action="store", help="Weeks; must be a positive whole number", type=int)
parser.add_argument('-o','--months', action="store", help="mOnths; must be a positive whole number", type=int)
parser.add_argument('-y','--years', action="store", help="Year; must be a positive whole number", type=int)
args = parser.parse_args()

def compare(s):     # These vars need to be globally accessible but how?
#    pdb.set_trace()
    x = 1
    while x == 1:
        if s > yearSecs:
            print("{} is > yearSecs".format(s))
            years = calcYears(s)
        elif s > monthSecs:
            print("{} is > monthSecs".format(s))
            months = calcMonths(s)
        elif s > weekSecs:
            print("{} is > weekSecs".format(s))
            weeks = calcWeeks(s)
        elif s > daySecs:
            print("{} is > daySecs".format(s))
            days = calcDays(s)
        elif s > hourSecs:
            h = calcHours(s)
            hours = h[0]
        elif s >= minSecs:
            print("{} is > minSecs".format(s))
            m = calcMins(s)[0]
            print("Minutes: %s" % m)
        elif calcMins(s)[1]:
            print("secs")
            seconds = calcMins(s)[1]
        x = 0


def printResults(s):
    print("{} is:\n".format(s))
    if years:
        print("{} years,\n".format(years))
    elif months:
        print("{} months,\n".format(months))
    elif weeks:
        print("{} weeks,\n".format(weeks))
    elif days:
        print("{} days,\n".format(days))
    elif hours:
        print("{} hours,\n".format(hours))
    elif mins:
        print("{} minutes,\n".format(mins))
    elif seconds:
        print("{} seconds,\n".format(seconds))





def calcYears(s):
    values = divmod(s,yearSecs)
    numYears = values[0]
    secsRemain = values[1]
    # leap year, add a day
    if numYears > 3:
        secsRemain += 86400
    return (numYears, secsRemain)

#pdb.set_trace()
def calcMonths(s):
    values = divmod(s,monthSecs)
    numMonths = values[0]
    secsRemain = values[1]
    return (numMonths, secsRemain)
    

#pdb.set_trace()
def calcWeeks(s):
    values = divmod(s,weekSecs)
    numWeeks = values[0]
    secsRemain = values[1]
    return (numWeeks, secsRemain)

#pdb.set_trace()
def calcDays(s):
    values = divmod(s,daySecs)
    numDays = values[0]
    secsRemain = values[1]
    return (numDays, secsRemain)  

#pdb.set_trace()
def calcHours(s):
    values = divmod(s,hourSecs)
    numHours = values[0]
    secsRemain = values[1]
    return (numHours, secsRemain)

#pdb.set_trace()
def calcMins(s):
    values = divmod(s,minSecs)
    numMins = values[0]
    secsRemain = values[1]
    if secsRemain > 0:
        return (numMins, secsRemain)
    else:
        return numMins

# determine who to call based on
compare(args.secs)
printResults(args.secs)
