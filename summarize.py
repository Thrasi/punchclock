#!/usr/bin/python

from datetime import datetime
from collections import defaultdict
import sys
import os
import argparse

parser = argparse.ArgumentParser(description='Summarize time logs.')
parser.add_argument('-c', '--case', help="Case number to summarize e.g. ABC-1234")
parser.add_argument('-f', '--files', nargs='+', help="Files to summarize")
args = parser.parse_args()

dates = defaultdict( lambda: defaultdict( float ) )
date_format='%Y-%m-%d %H-%M-%S'
target_case=""
FILES=os.listdir("logs")
case_total = 0

if args.files != None:
	FILES = args.files

if args.case != None:
	target_case = args.case

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
            	print "-----------------------------------------"
                print "{}:".format(date)
                print "\t{:<15}{:04.2f}".format( target_case, dates[date][target_case] )
                case_total += dates[date][target_case]
if target_case!="":
        print
        print "Total hours on {:<12}{:04.2f}".format( str(target_case)+":", case_total )
        print "-----------------------------------------"


