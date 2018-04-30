#!/usr/bin/python

from datetime import datetime
from collections import defaultdict
import sys

def summarize_hours( hour_log ):
	pass

#FILE_PATH = "/home/mb/Documents/scripts/punchclock/hour_log.txt"
FILE_PATH = "/home/mb/aphelion/hours/punchclock/hour_log.txt"
dates = defaultdict( lambda: defaultdict( float ) )
date_format='%Y-%m-%d %H-%M-%S'
target_case=""
case_total = 0
if len(sys.argv) > 1:
        target_case = sys.argv[1]

with open( FILE_PATH ) as f:
	for entry in f.readlines()[1:]:
#                print entry
		[ case, start_time_str, end_time_str ]  = entry.split( "\t" )
		start_date = datetime.strptime( start_time_str.strip(), date_format )
		end_date = datetime.strptime( end_time_str.strip(), date_format )
		duration = end_date - start_date
		hours = ( duration.seconds // 3600 ) + ( duration.seconds % 3600 / 3600.0 )
		dates[ str(start_date.date()) ][ case.strip() ] += hours

for date in sorted( dates.keys() ):
	day_total = 0
        if target_case=="":
	        print "{}:".format(date)
	        for case in sorted( dates[date] ):
		        print "\t{:<15}{:04.2f}".format( case, dates[date][case] )
		        day_total += dates[date][case]
                print
                print "Total hours on {:<12}{:04.2f}".format( str(date)+":", day_total )
                print
        else:
                if target_case in dates[date]:
                        print "{}:".format(date)
                        print "\t{:<15}{:04.2f}".format( target_case, dates[date][target_case] )
                        case_total += dates[date][target_case]
if target_case!="":
        print
        print "Total hours on {:<12}{:04.2f}".format( str(target_case)+":", case_total )
        print


