 
#For itembuild.csv, creates a csv with:
#Buildname, Champion, role, build


#Doing that import thing. This is the library for requesting the stuff, opening the response
#   that has the stuff, and handling errors if it didn't want to give us the stuff.
from urllib2 import Request, urlopen, URLError
#Import for creating a directory to store the files in so that we don't end up with a
#   bunch of messy csv files every time we run this thing.
from os import path, makedirs, getcwd
import csv


ggtoken = 'ad7c8fe0625bea8067333db89d12dedc' #My api token for champion.gg
folderpath = '/CSV Files' #Local folder for csv files
ggroot = 'http://api.champion.gg'

#Stuff to get names to iterate over.
urlnames = '/champion?api_key={0}'
champnameslist = []

urlwinning = '/champion/{0}/items/finished/mostWins?apikey={1}'
urlpopular = '/champion/{0}/items/finished/mostPopular?api_key={1}'

fieldnames = ['Buildname', 'Champion', 'role', 'build']

if not path.exists(getcwd()+folderpath):
    makedirs(getcwd()+folderpath)

csvfile = open(getcwd()+folderpath+'/itembuild.csv', 'wb')
wr = csv.writer(csvfile, quoting=csv.QUOTE_ALL)

tothecsv = []
tothecsv.append(fieldnames)

#requests the names
request = Request(ggroot + urlnames.format(ggtoken), headers={'User-Agent' : 'Magic Browser'})

response = urlopen(request).read() #opens the stuff for reading
for item in response.split('key":"')[1:]:#prepares for iteration, strips off first index because I like my lists naked from the waist up
    champnameslist.append(item[:item.find('"')])#the name is surrounded by " so it slices before the second "

i=0

for name in champnameslist:
	if i % 5 == 0:
		print "{0} of {1} champions have been processed".format(champnameslist.index(name), len(champnameslist))
	i+=1
	win = urlopen(Request(ggroot + urlwinning.format(name, ggtoken), headers={'User-Agent' : 'Magic Browser'})).read().split('"items":')[1:]
	popular = urlopen(Request(ggroot + urlpopular.format(name, ggtoken), headers={'User-Agent' : 'Magic Browser'})).read().split('"items":')[1:]
	for item in win:
		temp = []
		temp.append('Most Winning Build')
		temp.append(name)
		temp.append(item[item.find('"role":"')+8:item.find('"',item.find('"role":"')+8)])
		temp.append(item[1:item.find(']')])
		if temp[3] != '':
			tothecsv.append(temp)	
	for item in popular:
		temp = []
		temp.append('Most Popular Build')
		temp.append(name)
		temp.append(item[item.find('"role":"')+8:item.find('"',item.find('"role":"')+8)])
		temp.append(item[1:item.find(']')])
		if temp[3] != '':
			tothecsv.append(temp)


for item in tothecsv:
    wr.writerow(item)
csvfile.close()
