import numpy as np
import pandas as pd
import segyio
from segysak.segy import segy_bin_scrape
import pathlib

''' ------------ Read SEGY file --------------------------'''
filename = "../DATA/0063_ESPIRITO_SANTO_39.0063-0100.STK_FIN.5.sgy"
filesegy = pathlib.Path(filename)
#print("PORRA", filesegy, filesegy.exists())

''' --------------Scrape binary headet'''

binheader = segy_bin_scrape(filesegy)
print (binheader.items())
print (binheader.keys())

b = list(binheader) 
print ("number of elements", len(b))

binheader["JobID"]=1000
binheader["ReelNumber"]=9999

print ("JobID = ",binheader["JobID"])
print ("LineNumber = ",binheader["LineNumber"])
print ("ReelNumber = ",binheader["ReelNumber"])
print ("Traces = ",binheader["Traces"])
print ("AuxTraces =",binheader["AuxTraces"])


