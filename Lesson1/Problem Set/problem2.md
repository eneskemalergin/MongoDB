# Solution for the problem 2

The task for the second problem in the first problem set is to create new csv file which values are seperated by the "|" delimiter. Output should look like this:

```
Station|Year|Month|Day|Hour|Max Load
COAST|2013|01|01|10|12345.6
EAST|2013|01|01|10|12345.6
FAR_WEST|2013|01|01|10|12345.6
NORTH|2013|01|01|10|12345.6
NORTH_C|2013|01|01|10|12345.6
SOUTHERN|2013|01|01|10|12345.6
SOUTH_C|2013|01|01|10|12345.6
WEST|2013|01|01|10|12345.6
```

We are only allowed to change the code in parse_file function and save_file function. Here is the code provided at the beginning:

```Python 
import xlrd
import os
import csv
from zipfile import ZipFile

datafile = "2013_ERCOT_Hourly_Load_Data.xls"
outfile = "2013_Max_Loads.csv"


def open_zip(datafile):
    with ZipFile('{0}.zip'.format(datafile), 'r') as myzip:
        myzip.extractall()


def parse_file(datafile):
    workbook = xlrd.open_workbook(datafile)
    sheet = workbook.sheet_by_index(0)
    data = None
    # YOUR CODE HERE
    # Remember that you can use xlrd.xldate_as_tuple(sometime, 0) to convert
    # Excel date to Python tuple of (year, month, day, hour, minute, second)
    return data

def save_file(data, filename):
    # YOUR CODE HERE

    
def test():
    open_zip(datafile)
    data = parse_file(datafile)
    save_file(data, outfile)

    number_of_rows = 0
    stations = []

    ans = {'FAR_WEST': {'Max Load': '2281.2722140000024',
                        'Year': '2013',
                        'Month': '6',
                        'Day': '26',
                        'Hour': '17'}}
    correct_stations = ['COAST', 'EAST', 'FAR_WEST', 'NORTH',
                        'NORTH_C', 'SOUTHERN', 'SOUTH_C', 'WEST']
    fields = ['Year', 'Month', 'Day', 'Hour', 'Max Load']

    with open(outfile) as of:
        csvfile = csv.DictReader(of, delimiter="|")
        for line in csvfile:
            station = line['Station']
            if station == 'FAR_WEST':
                for field in fields:
                    # Check if 'Max Load' is within .1 of answer
                    if field == 'Max Load':
                        max_answer = round(float(ans[station][field]), 1)
                        max_line = round(float(line[field]), 1)
                        assert max_answer == max_line

                    # Otherwise check for equality
                    else:
                        assert ans[station][field] == line[field]

            number_of_rows += 1
            stations.append(station)

        # Output should be 8 lines not including header
        assert number_of_rows == 8

        # Check Station Names
        assert set(stations) == set(correct_stations)

        
if __name__ == "__main__":
    test()

```

We will start with parsing the file that we have already, '2013_ERCOT_Hourly_Load_Data.xls'. We need to open it up and parse it into Python first to use it for further instruction. Here is my approach:

```Python 
def parse_file(datafile):
	# Opens up the data file to work on
    workbook = xlrd.open_workbook(datafile)
    # we specifiy the worksheet
    sheet = workbook.sheet_by_index(0)
    # Initial empty dictionary to store the data init.
    data = {}
    # Iterate over the columns in the specified worksheet
    for i in range(1,sheet.ncols-1):
    	# get the cell value in first row and ith column and store it into variable station
        station = sheet.cell_value(0,i)
        # slice the value from ith row and all column and store it into variable d
        d = sheet.col_values(i, start_rowx = 1, end_rowx = None)
        # gets the maximum of d and store it into maxi
        maxi = max(d)   
        # get the date of maxi     
        maxiDate = xlrd.xldate_as_tuple(sheet.cell_value(d.index(maxi) + 1, 0),0)[:-2]
        # store the maxi and maxi date into the dictionary as follows.
        data[station] = {"maxi" : maxi, "maxiDate" : maxiDate}     
        # Iterate over when maximum column reached
    # Return the data.
    return data  
```
Now we are done with parsing our data into Python, then we can use it. What want to achive was to save the parsed data into csv file with delimiter "|". Here is the csv creator function.

```Python
def save_file(data, filename):
	# opens file for writing
   with open(filename, "w") as q:
   		# csv.writer method has parameter which you can define delimiter as this: delimiter = '|'
        w = csv.writer(q, delimiter = '|')
        # Writes the row of corresponding
        w.writerow(["Station", "Year", "Month", "Day", "Hour", "Max Load"])
        # iterate over data
        for each in data:
        	# Save the date as in year month, day, hour format.
            year, month, day, hour = data[each]['maxiDate']
            # Then write that format also.
            w.writerow([each, year, month, day, hour, data[each]['maxi']])
```
