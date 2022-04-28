#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# This is an application which will take a number
# of seconds as an argument and will calculate how
# many years, months, weeks, days, hours, minutes and
# seconds that the seconds entered is equivalent to

import argparse
import logging

# Variables
years, months, weeks, days, hours, minutes, seconds, leap_yrs = 0, 0, 0, 0, 0, 0, 0, 0
t = {"y":0, "m":0, "w":0, "d":0, "h":0, "i":0, "s":0}
values = []
leap_yr_bool = False

# Set up logging
logging.basicConfig(format='%(levelname)s:%(message)s', filename='example.log', level=logging.DEBUG)


def main():
    parser = argparse.ArgumentParser(description='Parse the arguments')
    parser.add_argument('-s', '--secs', action="store", help="Seconds; must be a positive whole number", type=int)
    # parser.add_argument('-m','--minutes', action="store",
    #        help="Minutes; must be a positive whole number", type=int)
    # parser.add_argument('-u','--hours', action="store",
    #        help="hoUrs; must be a positive whole number", type=int)
    # parser.add_argument('-d','--days', action="store",
    #        help="Days; must be a positive whole number", type=int)
    # parser.add_argument('-w','--weeks', action="store",
    #       help="Weeks; must be a positive whole number", type=int)
    # parser.add_argument('-o','--months', action="store",
    #        help="mOnths; must be a positive whole number", type=int)
    # parser.add_argument('-y','--years', action="store",
    #        help="Year; must be a positive whole number", type=int)
    if not parser.parse_args():
        # Ask user for number of seconds
        try:
            s = input("Seconds: ")
        finally:
            print("I can't accept input like that, so I'm exiting now, please try again.")
            exit(1)
    else:
        args = parser.parse_args()
        s = args.secs
    compare(s)

def calc_leap_year_days(t):
    # This gets called when the years is a multiple of 4 (x % 4 == 0)
    # t is years (4, 8, 12, 16, etc.)
    def bool_t(boo): # to set leap_yr_bool a couple of lines down
        boo = True
        return boo
    global leap_yr_bool
    leap_yr_bool = bool_t(True)
    secs_in_day = 86400
    if t > 3:  # t should be at least 4 but check anyway
        v = secs_in_day * (t//4)    
        global leap_years
        leap_years = int(t//4)
    return v

def compare(z):
    # The value being passed in is at least what unit?
    secs_in_year = 31556952
    secs_in_month = 2629746
    secs_in_week = 604800
    secs_in_day = 86400
    secs_in_hour = 3600
    secs_in_min = 60
    if z >= secs_in_year:
        values = divmod(z, secs_in_year)  # values is a tuple but be two variables
        t['y'] = values[0]
        if values[0] > 3:
            calc_leap_year_days(values[0])
            r = int(values[1] + calc_leap_year_days(values[0]))
            compare(r)
        else:    
            compare(values[1])
    elif z >= secs_in_month:
        values = divmod(z, secs_in_month)
        t['m'] = values[0]
        compare(values[1])
    elif z >= secs_in_week:
        values = divmod(z, secs_in_week)
        t['w'] = values[0]
        compare(values[1])
    elif z >= secs_in_day:
        values = divmod(z, secs_in_day)
        t['d'] = values[0]
        compare(values[1])
    elif z >= secs_in_hour:
        values = divmod(z, secs_in_hour)
        t['h'] = values[0]
        compare(values[1])
    elif z >= secs_in_min:
        values = divmod(z, secs_in_min)
        t['i'] = values[0]
        t['s'] = (values[1])
    else:
        seconds = z
        t['s'] = z

def print_output():
    if leap_yr_bool and t['y']:
        print(f"Years: {t['y']} (Leap Years: {leap_years})")
    if t['y'] and not leap_yr_bool:
        print(f"Years: {t['y']}")
    if t['m']:
        print(f"Months: {t['m']}")
    if t['w']:
        print(f"Weeks: {t['w']}")
    if t['d']:
        print(f"Days: {t['d']}")
    if t['h']:
        print(f"Hours: {t['h']}")
    if t['i']:
        print(f"Minutes: {t['i']}")
    if t['s']:
        print(f"Seconds: {t['s']}")

if __name__ == '__main__':
    main()
    print_output()
