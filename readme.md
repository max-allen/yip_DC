To run, please pip or conda install the dependencies imported at the top of the file.
'python parsedata.py' will start the script.

I chose Python's pandas library for the data-munging / analysis work here. It structures the
data and comes equipped with a few methods that allowed me to easily manipulate the data as
necessary. Otherwise, just making good use of regular expressions allowed me to get the data
in a palatable format I could average.

If no budget was found for an winner, a "NR" placeholder (not reported) is in it's place.

There was one entry where the budget was reported as a range. I took the conservative figure on the 
lower end of the range.