'''
Created on 2012-11-3

@author: zxy
'''
import re


DATAPATH = "./data/data.txt"
STOPWORDPATH = "./data/stopword.dat"
FEATUREPATH = "./data/feature.dat"

def Readfile():
	try:
		datafile = open(DATAPATH,"r")
		data = datafile.readlines()
		datafile.close()
	except Exception, e:
		print "[Error]Cant open data file."
		return 0
	return data


def Setup_wordlist(datalist):
	REG = re.compile('[a-zA-Z]+')
	data = " ".join(datalist)
	wordlist = sorted(list(set(re.findall(REG,data.lower()))))
	print "[Info]Number of features:%d" % len(wordlist)
	return wordlist


def Del_stopword(wordlist):
	try:
		stopwordfile = open(STOPWORDPATH,"r")
		stopwordlist = stopwordfile.readlines()
		stopwordfile.close()
		wordlist = list(set(wordlist) - set(stopwordlist))
		print "[Info]Number of features without stopwords:%d" % len(wordlist)
	except Exception, e:
		print "[Info]Can't open stopword file."
		return 0
	return wordlist


def Setup_feature(wordlist,data,data_num):
	"""setup feature for dlsi. write to feature.txt"""
	featurefile = open(FEATUREPATH,"w")
	length = len(wordlist)
	for i in xrange(data_num):
		words = data[i]
		line = ""
		for index in xrange(length):
			if wordlist[index] in words:
				line += str(index) + ":" + str(words.count(wordlist[index])) + " "
		line += "\n"
		featurefile.write(line)
	featurefile.close()


def preprocess():
	print "[Info]preprocess start."
	
	data = Readfile()
	doc_num = (int)(data[0])
	print "[Info]Number of documents:%d" % doc_num
	wordlist = Setup_wordlist(data[1:])
	wordlist = Del_stopword(wordlist)
	Setup_feature(wordlist,data[1:],doc_num)

	print "[Info]preprocess complete."


if __name__ == "__main__":
	preprocess()