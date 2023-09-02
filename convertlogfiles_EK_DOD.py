#!/usr/bin/python
from __future__ import division
import sys
import os
import re
import numpy as np

#command line options
if (len(sys.argv) < 2):
	print "\n\tusage: %s <subject>\n" % sys.argv[0]
	sys.exit()
else:
	subject = sys.argv[1]	

#set paths
pathbase = "/Volumes/AZLab/AON_tasks/fmri_data/%s/logfiles" % subject
files = os.listdir(pathbase)
files = [elem for elem in files if "maindesign" in elem]
print "Maindesign files:"
print files

for logfilename in files:
	fullpath = os.path.join(pathbase,logfilename)

	pattern = "LA\d+_(ASD|TD|DCD)_(Disgust|DISGUST|DIS)_\d*_(\d?)_maindesign.txt"
	print logfilename
	result = re.match(pattern,logfilename)
	# print result
	
	# task = "Dis"




	# pattern = "LA\d+_(P1|ASD|TD|DCD)_(.*?)_*_(\d?)_maindesign.txt"
	# result = re.match(pattern,logfilename)
	if result:
		# task = result.groups()[1]
		task = "DIS"
		run = int(result.groups()[2])
		print task
		print run

		logfile = open(fullpath)
		lines = logfile.readlines()
		numlines = lines.__len__() 
		print "Working on file %s task %s  lines: %d" % (logfilename,task,numlines)

		# pastjunk = 0
		firstofblock = 1

		if numlines > 100:
			for line in lines:
				if line.__len__() > 1:
					(condition,onset) = line.split()
					# print condition
					# print onset

					if (condition == "NeutralFood") or (condition == "Neutral") or (condition == "DisgustFood") or (condition == "Disgust"):
						if firstofblock:
							blockcondition = condition
							blockonset = float(onset)
							firstofblock = 0
					if condition == "Control":
						# pastjunk = 1
						firstofblock = 1
						duration = float(onset) - blockonset
						print "Condition: %s Onset %.2f Duration %.2f" % (blockcondition,blockonset,duration)
						outfilename = "%s/%s_%s_%d_%s.txt" % (pathbase,subject,task,run,blockcondition)
						outfile = open(outfilename,"a")
						outfile.write("%.2f %.2f 1\n" % (blockonset,duration))
					else:
						if firstofblock:
							blockcondition = condition
							blockonset = float(onset)
							firstofblock = 0	
					# else:
					# 	if condition == "Control":
					# 		firstofblock = 1
					# 		duration = float(onset) - blockonset
					# 		print "Condition: %s Onset %.2f Duration %.2f" % (blockcondition,blockonset,duration)
					# 		outfilename = "%s/%s_%s_%d_%s.txt" % (pathbase,subject,task,run,blockcondition)
					# 		outfile = open(outfilename,"a")
					# 		outfile.write("%.2f %.2f 1\n" % (blockonset,duration))
					# 	else:
					# 		if firstofblock:
					# 			blockcondition = condition
					# 			blockonset = float(onset)
					# 			firstofblock = 0
	else:
		print "*****File does not have enough lines, will be ignored"
