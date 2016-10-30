#!/usr/bin/env python

'''
Written by: Mike Hauss

This script accepts a whole number as a number of seconds and tells how many years, months, days,
weeks, days, hours, minutes and seconds it is equal to.
'''
import pdb
import argparse

# Variables
secsCalYear = 31536000  # seconds per calendar year
secsIn30DayMonth = 2592000
secsInWeek = 604800
secsInDay = 86400
secsInHour = 3600
secsInMin = 60
numYears = 0
numMonths = 0
numWeeks = 0
numDays = 0
numHours = 0
numMins = 0
seconds = 0 # initialize to zero (stores main input)
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

def compare(s):
#    pdb.set_trace()
    x = 1
    while x == 1:
        if s > secsCalYear:
            calcYears(s)
        elif s > secsIn30DayMonth:
            calcMonths(s)
        elif s > secsInWeek:
            calcWeeks(s)
        elif s > secsInDay:
            calcDays(s)
        elif s > secsInHour:
            calcHours(s)
        elif s > secsInMin:
            calcMins(s)
        else:
            secsRemain = s
        x = 0

'''
This is where we determine how many seconds we're dealing with and what time frame we have.
'''



def printResults():
    print("{} is:\n".format(y))


'''
Take input already determined to be > 1 calendar year.  There's an extra day every fourth year, so if numYears > 3,
we'll use secsCalLeap in our calculations.  We'll then obtain both how many years we have AND the remainder.
Subtract numYears * 
secsCalYear=31536000  # seconds per calendar year
from input to get the remainder in seconds.
At this point, we'll have populated the numYears var with how many years and returned the remaining seconds.
'''
def calcYears(s):
    p = s % secsCalYear
    numYears = s - (s - p)   # population of this variable is the central point of this function
    secsRemain = p
    if numYears > 3:
        secsRemain += 86400     # add a day to the remaining seconds (for leap year)
    compare(secsRemain)


'''
Take input already determined to be > 1 month.  We'll then obtain both how many months we have AND the remainder.
Subtract (numMonths * 2592000) from input to get the remainder in seconds.
At this point, we'll have populated the numMonths var with how many years and returned the remaining seconds.
'''
#pdb.set_trace()
def calcMonths(s):
    secsRemain = (s % secsIn30DayMonth) 
    numMonths = s - secsRemain
    compare(secsRemain)

#pdb.set_trace()


'''
Take input already determined to be > 1 week or, 7 * 86400.  We'll then obtain both how many days we have AND the remainder.
Subtract (numWeeks * 86400) from input to get the remainder in seconds.
At this point, we'll have populated the numYears var with how many years and returned the remaining seconds.
'''
def calcWeeks(s):
    secsRemain = (s % secsInWeek)
    numWeeks = s/secsInWeek
    compare(secsRemain)


'''
Take input already determined to be > 1 day. We'll then obtain both how many days we have AND the remainder.
Subtract (numDays * 86400) from input to get the remainder in seconds.
At this point, we'll have populated the numYears var with how many years and returned the remaining seconds.
'''
#pdb.set_trace()
def calcDays(s):
    numDays = s/secsInDay
    secsRemain = s - (numDays * secsInDay) 
    compare(secsRemain)
   

'''
Take input already determined to be > 1 hour. We'll then obtain both how many hours we have AND the remainder.
Subtract (numHours * 3600) from input to get the remainder in seconds.
At this point, we'll have populated the numYears var with how many years and returned the remaining seconds.
'''
#pdb.set_trace()
def calcHours(s):
    numHours = s/secsInHour
    secsRemain = s - (numHours * secsInHour) 
    compare(secsRemain)
   

'''
Take input already determined to be > 1 minute. We'll then obtain both how many minutes
we have AND the remainder.  Subtract (numMins * 60) from input to get the remainder in seconds.
At this point, we'll have populated the numMins var with how many minutes and returned the remaining seconds.
'''
#pdb.set_trace()
def calcMins(s):
    numMins = s/secsInMin
    secsRemain = s - (numMins * secsInMin)


# determine who to call based on what's set
if args.secs:
    compare(args.secs)
elif args.mins:
    calcMins(args.mins)
elif args.hours:
    calcHours(args.hours)
elif args.days:
    calcDays(args.days)
elif args.weeks:
    calcWeeks(args.weeks)
elif args.months:
    calcMonths(args.months)
else: 
    calcYears(args.years)

x = 1
while x == 1:
    if numYears:
        y = numYears
    elif numMonths:
        y = numMonths
    elif numWeeks:
        y = numWeeks
    elif numDays:
        y = numDays
    elif numHours:
        y = numHours
    elif numMins:
        y = numMins
    else:
        y = secsRemain
        x = 0

printResults()
