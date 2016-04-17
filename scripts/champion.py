#For role.csv, creates a csv with:
#Champion, lane, win_rate, kills, deaths, assists, minions_killed


#Doing that import thing. This is the library for requesting the stuff, opening the response
#       that has the stuff, and handling errors if it didn't want to give us the stuff.
from urllib2 import Request, urlopen, URLError
#Import for creating a directory to store the files in so that we don't end up with a
#       bunch of messy csv files every time we run this thing.
from os import path, makedirs, getcwd
import csv

riottoken = '180d011c-06d3-4722-9eef-3a3de8d6bc83' #My api token for riotgames
ggtoken = 'ad7c8fe0625bea8067333db89d12dedc' #My api token for champion.gg
folderpath = '/CSV Files' #Local folder for csv files
riotroot = 'https://na.api.pvp.net/api'
ggroot = 'http://api.champion.gg'

#Stuff to get names to iterate over.
urlnames = '/champion?api_key={0}'
champnameslist = []

#Exact location of url for skills and fields desired from it
urlskills = '/champion/{0}/skills?api_key={1}'
fieldskills = ['Qname', 'Wname', 'Ename', 'Rname']
fieldskillnames = ['name','image_location', 'q_skill', 'w_skill', 'e_skill', 'r_skill']

#Exact location of url for images
urlimages = '/lol/static-data/NA/v1.2/champion'

if not path.exists(getcwd()+folderpath):
    makedirs(getcwd()+folderpath)

csvfile = open(getcwd()+folderpath+'/champion.csv', 'wb')
wr = csv.writer(csvfile, quoting=csv.QUOTE_ALL)

tothecsv = [[]]
for item in fieldskillnames:
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
    requestskills = Request(ggroot + urlskills.format(name, ggtoken), headers={'User-Agent' : 'Magic Browser'})
    responseskills = urlopen(requestskills).read().split('name":"')[1:]
    temp = []
    temp.append(name)
    temp.append("")
    for item in responseskills:
        temp.append(item[:item.find('"')])
    tothecsv.append(temp)
for item in tothecsv:
    wr.writerow(item)
csvfile.close()
