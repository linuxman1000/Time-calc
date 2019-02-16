#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Written by: Mike Hauss

This script accepts a whole number as a number of seconds and tells how many
years, months, days, weeks, days, hours, minutes and seconds it is equal to.
If the argument is -m; -u; -d; -w and/or -y, tell how many seconds
'''
import argparse

# Variables
secs_in_year = 31536000
secs_in_month = 2592000  # 30 day month
secs_in_week = 604800
secs_in_day = 86400
secs_in_hour = 3600
secs_in_min = 60

# This just initializes everyone to null
years, months, weeks, days, hours, mins, seconds, secs_remain, subtotal = '','','','','','','','',''

def main():   # parses input
    # Take input
    parser = argparse.ArgumentParser()
    parser.add_argument('-s','--secs', action="store",
            help="Seconds; must be a positive whole number", type=int)
    parser.add_argument('-m','--mins', action="store",
            help="Minutes; must be a positive whole number", type=int)
    parser.add_argument('-u','--hours', action="store",
            help="hoUrs; must be a positive whole number", type=int)
    parser.add_argument('-d','--days', action="store",
            help="Days; must be a positive whole number", type=int)
    parser.add_argument('-w','--weeks', action="store",
            help="Weeks; must be a positive whole number", type=int)
    parser.add_argument('-o','--months', action="store",
            help="mOnths; must be a positive whole number", type=int)
    parser.add_argument('-y','--years', action="store",
            help="Year; must be a positive whole number", type=int)
    args = parser.parse_args()
    global in_secs # how many seconds we entered on CLI

    '''
    If we passed (an) amount(s) of time other than seconds, find out
    which one(s) and call the appropriate function(s)
    '''
    # Calculate Values
    if args.mins:
        subtotal += calc_secs(secs_in_min,args.mins)
    if args.hours:
        subtotal += calc_secs(secs_in_hour,args.hours)
    if args.days:
        subtotal += calc_secs(secs_in_day,args.days)
    if args.weeks:
        subtotal += calc_secs(secs_in_week,args.weeks)
    if args.months:
        subtotal += calc_secs(secs_in_month,args.months)
    if args.years:
        subtotal += calc_secs(secs_in_year,args.years)
    if args.secs:
        in_secs = args.secs # declared here so it can be referenced outside of main
    compare(args.secs)

def compare(u):
    global years, months, weeks, days, hours, mins, seconds, secs_remain
    if u > secs_in_year:
	    values = divmod(u,secs_in_year)     # returns a list
	    years = values[0]            # whole number
	    secs_remain = values[1]          # remainder
	    # leap year, add a day
	    if years > 3:
		secs_remain += 86400
            years = calc_years(u)[0]
            secs_remain = calc_years(u)[1]
            compare(secs_remain)
    elif u > secs_in_month:
        months = calc_months(u)[0]
        secs_remain = calc_months(u)[1]
        compare(secs_remain)
    elif u > secs_in_week:
        weeks = calc_weeks(u)[0]
        secs_remain = calc_weeks(u)[1]
        compare(secs_remain)
    elif u > secs_in_day:
        days = calc_days(u)[0]
        secs_remain = calc_days(u)[1]
        compare(secs_remain)
    elif u > secs_in_hour:
        values = divmod(u,secs_in_hour)
        hours = values[0]
	secs_remain = values[1]
        #hours = calc_hours(u)[0]
        #secs_remain = calc_hours(u)[1]
        compare(secs_remain)
    elif u >= secs_in_min:
        mins = calc_mins(u)[0]
        secs_remain = calc_mins(u)[1]
        compare(secs_remain)
    else:
        seconds = u


# each of these is a list with remaining time as [1]
def calc_years(s):
    values = divmod(s,secs_in_year)     # returns a list
    num_years = values[0]            # whole number
    remainder = values[1]          # remainder
    # leap year, add a day
    if num_years > 3:
        remainder += 86400
    return [num_years, remainder]

def calc_months(s):
    values = divmod(s,secs_in_month)
    return [values[0], values[1]]

def calc_weeks(s):
    values = divmod(s,secs_in_week)
    return [values[0], values[1]]

def calc_days(s):
    values = divmod(s,secs_in_day)
    return [values[0], values[1]]
def calc_hours(s):
    values = divmod(s,secs_in_hour)
    return [values[0], values[1]]
def calc_mins(s):
    values = divmod(s,secs_in_min)
    return [values[0], values[1]]

def calc_secs(x,y):
    product = (x*y)
    subtotal += product
    return subtotal

if __name__ == '__main__':
    main()
'''
To Do:
Print one statement if seconds and the other if anything else
'''
if seconds:
   print "%s seconds is equivalent to: " % (in_secs)
if years:
    if years > 1:
        print "%s Years" % (years)
    else:
        print "%s Year" % (years)
if months:
    if months > 1:
        print "%s Months" % (months)
    else:
        print "%s Month" % (months)
if weeks:
    if weeks > 1:
        print "%s Weeks" % (weeks)
    else:
        print "%s Week" % (weeks)
if days:
    if days > 1:
        print "%s Days" % (days)
    else:
        print "%s Day" % (days)
if hours:
    if hours > 1:
        print "%s Hours" % (hours)
    else:
        print "%s Hour" % (hours)
if mins:
    if mins > 1:
        print "%s Minutes" % (mins)
    else:
        print "%s Minute" % (mins)
if seconds:
    if seconds > 1:
        print "%s Seconds" % (seconds)
    else:
        print "%s Second" % (seconds)
elif args.year or args.month or args.week or args.day or args.hour:
    if args.year > 1:
        print "%s years"
    elif args.year:
        print "%s year"
    else:
	print "You didn't enter \"seconds\""
