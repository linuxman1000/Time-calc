#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
This is an application which will take a number of seconds as an argument and 
will calculate how many years, months, weeks, days, hours, minutes and seconds
that the seconds entered is equivalent to
"""
import logging

# Variables
s, years, months, weeks, days, hours, minutes, seconds, leap_yrs = 0, 0, 0, 0, 0, 0, 0, 0, 0
leap_yr_bool = False
values = []
t = {"years":0, "months":0, "weeks":0, "days":0, "hours":0, "minutes":0, "seconds":0}

# Set up logging
logging.basicConfig(format='%(levelname)s:%(message)s', filename='timecalc.log', level=logging.DEBUG)
logger = logging.getLogger()

def main():
    """
    This is where the application begins executing
    """
    global s
        # Ask user for number of seconds
    try: 
        s = int(input("Seconds: "))
        if s < 0:
            raise Exception
    except Exception as err:
        print(f"The value {s} is invalid.")
        logger.error(err)
        exit(1) 
    else:  # What to do when the try block suceeds
        compare(s)


def calc_leap_year_days(t):
    """
    This takes one argument, t and gets called when years > 3.
    Therefore, if the argument is 4, 5, 6, 7, 8, 9... the output is how
    many times 4 divides into t, ignoring the remainder.
    Example:
    1) t = 11
       11/4 = 2 (remainder 3 ignored)

    2) t = 12
       12/4 = 3 (remainder 0 ignored)

    It contains a sub-function called bool_t that takes an argument, boo.
    The job of this function is to set the value of leap_yr_bool to True.
    This exists mainly for the print_output() function.

    """
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
        #c_to_f = lambda data: (data[0], (9/5*data[1] + 32)
        # yields iterable that must be converted to a list
        # list(map(c_to_f, temps)

def compare(z):
    """
    This function does the actual work of computing how much of each period
    an amount of seconds is.  It takes one argument, z (seconds) and is called
    by the parser above.  It checks the value against seconds in a year, month,
    week, day, hour and minute.  It uses divmod to compute out each value; it
    then passes each "remainder" back into itself until it gets down to the
    lowest value, seconds.
    It computes the leap year, which happens when years > 3, by calling the
    calp_leap_year_days function when years > 3.  Each iteration populates
    the t{} dictionary with keys and values of each respective time and value.
    """
    # The value being passed in is at least what unit?
    years, months, weeks, days, hours, minutes = (31556952, 2629746, 604800, 86400, 3600, 60)
    if z >= years:
        values = divmod(z, years)  # values is a tuple but contains two variables
        t['years'] = values[0]
        if values[0] > 3:
            calc_leap_year_days(values[0])
            r = int(values[1] + calc_leap_year_days(values[0]))
            compare(r)
        else:    
            compare(values[1])
    elif z >= months:
        values = divmod(z, months)
        t['months'] = values[0]
        compare(values[1])
    elif z >= weeks:
        values = divmod(z, weeks)
        t['weeks'] = values[0]
        compare(values[1])
    elif z >= days:
        values = divmod(z, days)
        t['days'] = values[0]
        compare(values[1])
    elif z >= hours:
        values = divmod(z, hours)
        t['hours'] = values[0]
        compare(values[1])
    elif z >= minutes:
        values = divmod(z, minutes)
        t['minutes'] = values[0]
        t['seconds'] = (values[1])
    else:
        seconds = z
        t['seconds'] = z
    return t

def print_output():
    """
    This prints the output of the t{} dictionary
    """
    i = compare(s)
    result = ""
    if i['years']:
      result = f"{i['years']} years, "
    if i['months']:
      result = result + f"{i['months']} months, "
    if i['weeks']: 
      result = result + f"{i['weeks']} weeks, "
    if i['days']:
      result = result + f"{i['days']} days, "
    if i['hours']:
      result = result + f"{i['hours']} hours, "
    if i['minutes']:
      result = result + f"{i['minutes']} minutes, "
      result = result + f"{i['seconds']} seconds. "
    else:
      result = result + f"{i['seconds']} seconds. "
    print(f"{s} seconds is: {result}")



if __name__ == '__main__':
    main()
    print_output()
