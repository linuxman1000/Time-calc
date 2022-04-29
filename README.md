# time_calculator.py

Written By: Mike Hauss (mikehauss at gmail dot com)

Converts seconds to bigger units (years, months, weeks, days, hours, minutes)
-s or --seconds is converted to years, months, weeks, days, hours, minutes and remaining seconds.
Everything else is converted to the equivalent seconds

How can this be useful?
This is useful anytime you have an amount of seconds and want to know how long ago x seconds was.  Many applications express time in seconds.  For example, DNS TTLs are expressed in seconds and many Linux utilities express an amount of time in seconds, even if it's been years.

## Requirements:
Python 3

_Notes:_ 

_1. This program is designed to be used on a CLI._

_2. This can easily be converted to work with Python 2.x; the main difference, in this case, is the print statements.  See the python 2.x branch._

## Usage:
(-s is the only option available at this time.  The other options will become available as the code is written.)
```
time_calculator.py [[-s][--seconds] seconds]

## Example:

arguments:
-s, --seconds SECONDS  A positive integer to be converted to larger time units.
If there are "remaining" seconds, they'll be shown as well.


There is still much to be done on this, so it is a work in progress.  However, feel free to use this.
```
