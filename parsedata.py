import requests as rq 
import locale
import pandas as pd
import re
from tabulate import tabulate

#request data
req = rq.get('redacted').json()
req = req['results']

films = []
years = []

for x in req:
	films.append(x['films'][0]) #winner is first object
	years.append(x['year'])

film_data = pd.DataFrame(films)
year_data = pd.DataFrame(years, columns=['Year'])

result = []

#get detailURL data
for x in film_data['Detail URL']:
	result.append(rq.get(x).json())

detail_data = pd.DataFrame(result)

#merge all data
all_data = pd.concat([film_data,detail_data['Budget'],year_data], axis=1)

# Not reported placeholder where no budget information is found
all_data.fillna('NR', inplace=True)

#Reduce information down to YYYY format
all_data.Year = all_data.Year.apply(lambda x: x[:4])

def parseData(string):
	numeric_pattern = re.compile(r'[^\d.]+')
	parsed = float(numeric_pattern.sub('', string))

	# standardizing 
	if parsed < 1000:
		return parsed * 1000000
	else:
		return parsed

all_data.Budget = all_data.Budget.str.replace('\[ [0-9] ]', '')
	
all_data.Budget = all_data.Budget.apply(lambda x: parseData(x) if x != 'NR' else 'NR')

#data to print
print_data = all_data.loc[:,['Year','Film','Budget']]

average = print_data[print_data['Budget'] != 'NR'].Budget.mean()

#currency setting for printing
locale.setlocale(locale.LC_ALL,'')

#print data and average
print tabulate(print_data,headers='keys')
print 'The average budget for winners is '+str(locale.currency(average, grouping=True))+'.'