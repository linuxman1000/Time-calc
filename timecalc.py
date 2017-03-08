# -*- coding: utf-8 -*-
#!/usr/bin/env python

'''
Written by: Mike Hauss

This script accepts a whole number as a number of seconds and tells how many
years, months, days, weeks, days, hours, minutes and seconds it is equal to.
If the argument is -m; -u; -d; -w and/or -y, tell how many seconds
'''
import pdb
import argparse

# Variables
year_secs = 31536000
month_secs = 2592000  # 30 day month
week_secs = 604800
day_secs = 86400
hour_secs = 3600
min_secs = 60
years = ''
months = ''
weeks = ''
days = ''
hours = ''
mins = ''
seconds = ''
secs_remain = ''

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
    in_secs = args.secs
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

#pdb.set_trace()
def calc_weeks(s):
    values = divmod(s,week_secs)
    return [values[0], values[1]]

#pdb.set_trace()
def calc_days(s):
    values = divmod(s,day_secs)
    return [values[0], values[1]]

#pdb.set_trace()
def calc_hours(s):
    values = divmod(s,hour_secs)
    return [values[0], values[1]]

#pdb.set_trace()
def calc_mins(s):
    values = divmod(s,min_secs)
    return [values[0], values[1]]

if __name__ == '__main__':
    main()
    print "%s seconds is equivalent to: \n%s Years\n%s Months\n%s Weeks\n%s Days\n%s Hours\n%s Minutes\n%s Seconds" % (in_secs, years, months, weeks, days, hours, mins, seconds)
