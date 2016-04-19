#For winrate.csv, creates a csv with:
#Champion1, Champion2, Champion1's winrate vs Champion2, role


#Doing that import thing. This is the library for requesting the stuff, opening the response
#       that has the stuff, and handling errors if it didn't want to give us the stuff.
from urllib2 import Request, urlopen
from urllib import urlretrieve
#Import for creating a directory to store the files in so that we don't end up with a
#       bunch of messy csv files every time we run this thing.
from os import path, makedirs, getcwd
import csv

ggtoken = 'ad7c8fe0625bea8067333db89d12dedc' #My api token for champion.gg
csvpath = '/CSV Files' #Local folder for csv files
ggroot = 'http://api.champion.gg'

fieldnames = ['Name', 'Opponent', 'role', 'winrate']
url = '/champion/{0}/matchup/?api_key={1}'

#Stuff to get names to iterate over.
urlnames = '/champion?api_key={0}'
champnameslist = []

if not path.exists(getcwd()+csvpath):
    makedirs(getcwd()+csvpath)

csvfile = open(getcwd()+csvpath+'/winrate.csv', 'wb')
wr = csv.writer(csvfile, quoting=csv.QUOTE_ALL)

tothecsv = [[]]
for item in fieldnames:
    tothecsv[0].append(item)

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
	response = urlopen(Request(ggroot + url.format(name, ggtoken), headers={'User-Agent' : 'Magic Browser'})).read().split('"role":"')[1]
	role = response[:response.find('"')]
	response = response.split('winRate":')[1:]
	for item in response:
		temp=[]
		temp.append(name)
		temp.append(item[item.find('"key":"')+7:item.find('"', item.find('"key":"')+7)])
		temp.append(role)
		temp.append(item[:item.find(',')])
		tothecsv.append(temp)

for item in tothecsv:
	wr.writerow(item)
csvfile.close()
