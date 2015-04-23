# Parsing CSV into Python without using any library
import os

directory = " "
datafile = "beatles-diskography.csv"

def parse_file(datafile):
	dat = [ ]
	with open(datafile, 'rb') as f:
		label = f.readline().split(",")
		c = 0
		for line in f:
			if c == 10:
				break

			fields = line.split(",")
			datadict = { }
            
			for i, value in enumerate(fields):
				datadict[label[i].strip()] = value.strip()

			dat.append(datadict)
			c += 1
	return dat



def test():
	dfile = os.path.join(directory, datafile)
	d = parse_file(dfile)

	# Checking if the algoritms work.
	firstline = {'Title': 'Please Please Me', 'UK Chart Position': '1', 'Label': 'Parlophone(UK)', 'Released': '22 March 1963', 'US Chart Position': '-', 'RIAA Certification': 'Platinum', 'BPI Certification': 'Gold'}
	tenthline = {'Title': '', 'UK Chart Position': '1', 'Label': 'Parlophone(UK)', 'Released': '10 July 1964', 'US Chart Position': '-', 'RIAA Certification': '', 'BPI Certification': 'Gold'}
	assert d[0] == firstline
	assert d[9] == tenthline

test()