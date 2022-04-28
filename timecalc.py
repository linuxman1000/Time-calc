#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Written by: Mike Hauss

This script accepts a whole number as a number of seconds and tells how many
years, months, days, weeks, days, hours, minutes and seconds it is equal to.
If the argument is -m; -u; -d; -w and/or -y, tell how many seconds
'''
import argparse
from datetime import date, time, timedelta, datetime

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
    s = args.secs
    m = args.mins
    u = args.hours
    d = args.days
    w = args.weeks
    o = args.months
    y = args.years
    compare(s,m,u,d,w,o,y)
    # Print results at end

#def compare(s,m,u,d,w,o,y):
    # Syntax: datetime.timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)
#    none_to_zero(s,m,u,d,w,o,y)
def compare(s,m,u,d,w,o,y):
    if s is None: s = 0
    if m is None: m = 0
    if u is None: u = 0
    if d is None: d = 0
    if w is None: w = 0
    if o is None: o = 0
    if y is None: y = 0
    print("Seconds: {a}, Minutes: {b}, Hours: {c}, Days: {x}, Weeks: {e}, Months: {f} Years: {g}".format(a=s,b=m,c=u,x=d,e=w,f=o,g=y))
# compare inputted time to each unit
'''
def compare(none_to_zero):
    y = timedelta(days=365)
    year_secs = y.total_seconds()
    m = timedelta(days=30)
    month_secs = m.total_seconds()
    w = timedelta(days=7)
    week_secs = w.total_seconds()
    d = timedelta(days=1)
    day_secs = d.total_seconds()
    h = timedelta(hours=1)
    hour_secs = h.total_seconds()
    i = timedelta(mins=1)
    min_secs = i.total_seconds()
   
    if u >= year_secs:
        values = divmod(u,year_secs)
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
'''
if __name__ == '__main__':
    main()
