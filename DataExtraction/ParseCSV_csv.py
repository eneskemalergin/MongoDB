import os
import csv
import pprint

directory = " "
datafile = "beatles-diskography.csv"

def parse_csv(datafile):
	data = []
	n = 0
	with open(datafile, 'rb') as sd:
		r = csv.DictReader(sd)
		for line in r:
			data.append(line)
	return data

if __name__ == "__main__":
	dfile = os.path.join(directory, datafile) 
	d = parse_csv(dfile)
	pprint.pprint(d)