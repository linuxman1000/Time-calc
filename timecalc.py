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
year_secs = 31536000
month_secs = 2592000  # 30 day month
week_secs = 604800
day_secs = 86400
hour_secs = 3600
min_secs = 60
years, months, weeks, days, hours, mins, seconds, secs_remain = '', '','','','','','',''
mi,h,d,w,mo,y,subtotal = 0,0,0,0,0,0,0

def main():   # parses input
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
    global in_secs

    '''
    If we passed in (an) amount(s) of time other than seconds, find out
    which one(s) and call the appropriate function(s)
    '''
    if args.mins:
        calc_secs(min_secs,args.mins)
        global mi
        mi = args.mins
    if args.hours:
        calc_secs(hour_secs,args.hours)
        global h
        h = args.hours
    if args.days:
        calc_secs(day_secs,args.days)
        global d
        d = args.days
    if args.weeks:
        calc_secs(week_secs,args.weeks)
        global w
        w = args.weeks
    if args.months:
        calc_secs(month_secs,args.months)
        global mo
        mo = args.months
    if args.years:
        calc_secs(year_secs,args.years)
        global y
        y = args.years
    in_secs = args.secs # declared globally here so it can be referenced outside of main
    compare(args.secs)

def sr(a):
    compare(a)

def compare(u):
    #pdb.set_trace()
    global years, months, weeks, days, hours, mins, seconds, secs_remain
    if u > year_secs:
        years = calc_years(u)[0]
        secs_remain = calc_years(u)[1]
        sr(secs_remain)
    elif u > month_secs:
        months = calc_months(u)[0]
        secs_remain = calc_months(u)[1]
        sr(secs_remain)
    elif u > week_secs:
        weeks = calc_weeks(u)[0]
        secs_remain = calc_weeks(u)[1]
        sr(secs_remain)
    elif u > day_secs:
        days = calc_days(u)[0]
        secs_remain = calc_days(u)[1]
        sr(secs_remain)
    elif u > hour_secs:
        hours = calc_hours(u)[0]
        secs_remain = calc_hours(u)[1]
        sr(secs_remain)
    elif u >= min_secs:
        mins = calc_mins(u)[0]
        secs_remain = calc_mins(u)[1]
        sr(secs_remain)
    else:
        seconds = u


# each of these is a list with remainder as [1]
def calc_years(s):
    values = divmod(s,year_secs)     # returns a list
    num_years = values[0]            # whole number
    remainder = values[1]          # remainder
    # leap year, add a day
    if num_years > 3:
        remainder += 86400
    return [num_years, remainder]

def calc_months(s):
    values = divmod(s,month_secs)
    return [values[0], values[1]]

def calc_weeks(s):
    values = divmod(s,week_secs)
    return [values[0], values[1]]

def calc_days(s):
    values = divmod(s,day_secs)
    return [values[0], values[1]]

def calc_hours(s):
    values = divmod(s,hour_secs)
    return [values[0], values[1]]

def calc_mins(s):
    values = divmod(s,min_secs)
    return [values[0], values[1]]

def calc_secs(x,y):
    product = (x*y)
    global subtotal
    subtotal += product

if __name__ == '__main__':
    main()
    message=""
    if seconds:
        print "%s seconds is equivalent to: \n%s Years\n%s Months\n%s Weeks\n%s Days\n%s Hours\n%s Minutes\n%s Seconds" % (in_secs, years, months, weeks, days, hours, mins, seconds)
    if calc_secs:
        print "%s minutes, %s hours, %s days, %s weeks, %s months, and %s years is equivalent to \n %s seconds" % (mi,h,d,w,mo,y,subtotal)
