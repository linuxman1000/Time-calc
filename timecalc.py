#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Written by: Mike Hauss

This script accepts a whole number as a number of seconds and tells how many
years, months, days, weeks, days, hours, minutes and seconds it is equal to.
If the argument is -m; -u; -d; -w and/or -y, tell how many seconds
'''
import argparse

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
    global s
    s = args.secs
    # m = args.mins
    # u = args.hours
    # d = args.days
    # w = args.weeks
    # o = args.months
    # y = args.years
    compare(s)
# variables
t = {} # dictionary that will hold timelabel:value pairs
print(t)

def compare(u):
    global t
    secs_in_year = 31556952
    secs_in_month = 2629746
    secs_in_week = 604800
    secs_in_day = 86400
    secs_in_hour = 3600
    secs_in_min = 60
    if u >= secs_in_year:
        values = divmod(u,secs_in_year)
        t['years'] = values[0]
        secs_remain = values[1]
        # leap year, add a day
        if values[0] > 3:
            secs_remain += secs_in_day
        compare(secs_remain)
    elif secs_in_month <= u <= secs_in_year:
        values = divmod(u,secs_in_month)  # divmod(x,y) returns a list (x / y, x % y)
        t['months'] = values[0]
        compare(values[1])
    elif secs_in_week <= u <= secs_in_month:
        values = divmod(u,secs_in_week)
        t['weeks'] = values[0]
        compare(values[1])
    elif secs_in_day <= u <= secs_in_week:
        values = divmod(u,secs_in_day)
        t['days'] = values[0]
        compare(values[1])
    elif secs_in_hour <= u <= secs_in_day:
        values = divmod(u,secs_in_hour)
        t['hours'] = values[0]
        compare(values[1])
    elif secs_in_min <= u <= secs_in_hour:
        values = divmod(u,secs_in_min)
        t['mins'] = values[0]
        compare(values[1])
    else:
        t['secs'] = u

if __name__ == '__main__':
    main()

print("{0} seconds is equivalent to: \n".format(s))
for unit,value in t.items():
    print("{} {}".format(value, unit))
