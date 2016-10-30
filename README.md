# timecalc.py

Written By: Mike Hauss mikehauss at gmail dot com

Converts seconds to bigger units (years, months, weeks, days, hours, minutes)
-s or --seconds is converted to years, months, weeks, days, hours, minutes and remaining seconds.
Everything else is converted to the equivalent seconds

## Requirements:
Python 3

_Note: This can easily be converted to work with Python 2.x; the main difference, in this case, is the print statements._

## Usage:

```
timecalc.py [[-s][--seconds] seconds]
            [[-m][--minutes] minutes]
            [[-u][--hours] hours]
            [[-d][--days] days]
            [[-w][--weeks] weeks]
            [[-o][--months] months]
            [[-y][--years] years]
arguments:
-s, --seconds SECONDS  A positive integer to be converted to larger time units.  If there are "remaining" seconds, they'll be shown as well.
The remaining options take a positive integer that is to be converted to seconds
-m, --minutes MINUTES
-u, --hours HOURS
-d, --days DAYS
-w, --weeks WEEKS
-o, --months MONTHS (30-day month used here)
-y, --years YEARS (accounts for leap years for every x % 4
```
