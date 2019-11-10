# -*- coding: utf-8 -*-
"""Data sanitizer

Simple script inspired from http://jmcauley.ucsd.edu/data/amazon/links.html
to convert the reviews and metadata compressed datasets to strict json.

"""

import json
import gzip

def sanitize(path, outpath):
	"""Converts a given json compressed to strict json and writes it in a new file

	Parameters
	----------
	path : str
	The file location of the gzip-compressed json file
	outpath : str
	The path to the desired output file location 

	"""
	g = gzip.open(path, 'r')

	out = open(outpath, 'w')

	for l in g:
		out.write(json.dumps(eval(l)) + '\n')
	out.close()
		
def main():
	meta_path = "meta_Grocery_and_Gourmet_Food.json.gz"
	reviews_path = "reviews_Grocery_and_Gourmet_Food.json.gz"
	
	meta_outpath = "cleaned_meta.json"
	reviews_outpath = "cleaned_reviews.json"
	
	sanitize(meta_path, meta_outpath)
	sanitize(reviews_path, reviews_outpath)
	
if __name__ == '__main__':
	main()
