#!/usr/bin/python

from datetime import datetime
from collections import defaultdict
import sys
import os
"""
python summarize.py 				: summarizes all days
python summarize.py [file]			: summarizes days from file
python summarize.py [file] [case]	: summarizes case from the file
"""
dates = defaultdict( lambda: defaultdict( float ) )
date_format='%Y-%m-%d %H-%M-%S'
target_case=""
FILES=[]         
case_total = 0
if len(sys.argv) > 1:
	FILES.append(sys.argv[1])
	if len(sys.argv) > 2:
 		target_case = sys.argv[2]
else:
	FILES=os.listdir("logs")

for file_path in FILES:
	with open( os.path.join("logs",file_path) ) as f:
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


