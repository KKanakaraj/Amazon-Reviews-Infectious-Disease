import sys
import gzip
import time

yearlist = []
countlist = []

def parseIterator(path):
	g = gzip.open(path, 'r')
	for l in g:
		yield eval(l)

def parseReviews(path):
	for review in parseIterator(path):
		year = review['reviewTime'].split()
		if year[2] not in yearlist:
			yearlist.append(year[2])
			countlist.append(1)
		else:
			index = yearlist.index(year[2])
			countlist[index] += 1

	for i in range(0, len(yearlist)):
		print str(yearlist[i]) + " - " + str(countlist[i])
		
def main(argv):
	directory = '/Users/home/Desktop/Data/'
	item = 'Amazon_Instant_Video'
	parseReviews(directory + 'reviews_' + item + '.json.gz')
	
if __name__ == '__main__':
	start_time = time.time()
	main(sys.argv)
	print 'Execution time is ' + str(time.time() - start_time) + ' seconds'