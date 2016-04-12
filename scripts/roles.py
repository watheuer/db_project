#Doing that import thing. This is the library for requesting the stuff, opening the response
#       that has the stuff, and handling errors if it didn't want to give us the stuff.
from urllib2 import Request, urlopen, URLError
#Import for creating a directory to store the files in so that we don't end up with a
#       bunch of messy csv files every time we run this thing.
from os import path, makedirs, getcwd
import csv


apitoken = 'ad7c8fe0625bea8067333db89d12dedc' #My api token for champion.gg
folderpath = '/CSV Files' #Local folder for csv files
csvfile = open(getcwd()+folderpath+'/roles.csv', 'wb')
wr = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
root = 'http://api.champion.gg'

#Stuff to get names to iterate over.
urlnames = '/champion?api_key={0}'
champnameslist = []

#Exact location of first url and fields desired from it
url1 = '/stats/champs/{0}?api_key={1}'
fields1 = ['role', 'winPercent', 'kills', 'deaths', 'assists', 'minionsKilled']
fieldnames1 = ['role', 'win_rate', 'kills', 'deaths', 'assists', 'minions_killed']

#Like above, but the second one. These are copy pasta-able.
url2 = '/champion/{0}/skills?api_key={1}'
fields2 = ['Qname', 'Wname', 'Ename', 'Rname']
fieldnames2 = ['q_skill', 'w_skill', 'e_skill', 'r_skill']

if not path.exists(getcwd()+folderpath):
        makedirs(getcwd()+folderpath)

tothecsv = [['Champion']]
for item in fields1:
        tothecsv[0].append(item)
for item in fields2:
        tothecsv[0].append(item)

#requests the names
request = Request(root + urlnames.format(apitoken), headers={'User-Agent' : 'Magic Browser'})

try:
        response = urlopen(request).read() #opens the stuff for reading
        for item in response.split('key":"')[1:]:#prepares for iteration, strips off first index because I like my lists naked from the waist up
                champnameslist.append(item[:item.find('"')])#the name is surrounded by " so it slices before the second "

except URLError, e:#should only ever be 404 error. If you get a 403... something went wrong with Request, I guess
        print 'Got an error code:', e 

i=0
#requests the first one
for name in champnameslist:
        if i % 5 == 0:
                print "{0} of {1} champions have been completed".format(champnameslist.index(name), len(champnameslist))
        i+=1
        request = Request(root + url1.format(name, apitoken), headers={'User-Agent' : 'Magic Browser'})
        request2 = Request(root + url2.format(name, apitoken), headers={'User-Agent' : 'Magic Browser'})
        response = urlopen(request).read()
        response2 = urlopen(request2).read().split('name":"')[1:]
        for item in response.split('role":"')[1:]:
                       temp = []
                       temp.append(name)
                       temp.append(item[:item.find('"')])
                       for field in fields1[1:]:
                               temp.append(item[item.find(field)+len(field)+2:item.find(',', item.find(field))].strip('}'))
                       for piece in response2:
                               temp.append(piece[:piece.find('"')])
                       tothecsv.append(temp)
for item in tothecsv:
        wr.writerow(item)
csvfile.close()
