# -*- coding: utf-8 -*-
"""FDA-Reviews data linking

Simple script that could be used to find corresponding FDA entries/Amazon products

"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import nltk

def filter_dist(x, y, threshold = 3):
	"""Determines if two given inputs are similar using the Levenshtein distance 

	Parameters
	----------
	x : str
	The first string
	y : str
	The second string
	threshold : int
	The threshold used to determine if the two inputs similar
	
	Returns
	-------
	boolean
		True if the strings are similar enough, false otherwise

	"""
	first = x.lower()
	second = y.lower() 
	
	return nltk.edit_distance(first, second) <= threshold
		
def main():
	pickle_file = "" #Assume an existing pickle exist containing the reviews and FDA merged dataframes
	
	columnA = "title" #First column to look up for similarity (here: title from metadata)
	columnB = "" #Second column to loop up for similarity (here: should be from FDA)
	
	df = pd.read_pickle(picke_file)
	
	df = df[df[[columnA, columnB]].apply(lambda x: filter_dist(*x), axis=1)]
	
if __name__ == '__main__':
	main()
