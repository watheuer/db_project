#For role.csv, creates a csv with:
#Champion, lane, win_rate, kills, deaths, assists, minions_killed


#Doing that import thing. This is the library for requesting the stuff, opening the response
#   that has the stuff, and handling errors if it didn't want to give us the stuff.
from urllib2 import Request, urlopen, URLError
#Import for creating a directory to store the files in so that we don't end up with a
#   bunch of messy csv files every time we run this thing.
from os import path, makedirs, getcwd
import csv


ggtoken = 'ad7c8fe0625bea8067333db89d12dedc' #My api token for champion.gg
folderpath = '/CSV Files' #Local folder for csv files
csvfile = open(getcwd()+folderpath+'/role.csv', 'wb')
wr = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
ggroot = 'http://api.champion.gg'

#Stuff to get names to iterate over.
urlnames = '/champion?api_key={0}'
champnameslist = []

#Exact location of first url and fields desired from it
urlstats = '/stats/champs/{0}?api_key={1}'
fieldstats = ['role', 'winPercent', 'kills', 'deaths', 'assists', 'minionsKilled']
fieldstatnames = ['lane', 'win_rate', 'kills', 'deaths', 'assists', 'minions_killed']

if not path.exists(getcwd()+folderpath):
    makedirs(getcwd()+folderpath)

tothecsv = [['Champion']]
for item in fieldstatnames:
    tothecsv[0].append(item)

#requests the names
request = Request(ggroot + urlnames.format(ggtoken), headers={'User-Agent' : 'Magic Browser'})

response = urlopen(request).read() #opens the stuff for reading
for item in response.split('key":"')[1:]:#prepares for iteration, strips off first index because I like my lists naked from the waist up
    champnameslist.append(item[:item.find('"')])#the name is surrounded by " so it slices before the second "

i=0
#requests the first one
for name in champnameslist:
    if i % 5 == 0:
        print "{0} of {1} champions have been processed".format(champnameslist.index(name), len(champnameslist))
    i+=1
    request = Request(ggroot + urlstats.format(name, ggtoken), headers={'User-Agent' : 'Magic Browser'})
    response = urlopen(request).read()
    for item in response.split('role":"')[1:]:
       temp = []
       temp.append(name)
       temp.append(item[:item.find('"')])
       for field in fieldstats[1:]:
           temp.append(item[item.find(field)+len(field)+2:item.find(',', item.find(field))].strip('}'))
       tothecsv.append(temp)
for item in tothecsv:
    wr.writerow(item)
csvfile.close()
