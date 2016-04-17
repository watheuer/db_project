#For item.csv, creates a csv with:
#ID, name, description, plaintext (which not all of them have)


#Doing that import thing. This is the library for requesting the stuff, opening the response
#       that has the stuff, and handling errors if it didn't want to give us the stuff.
from urllib2 import Request, urlopen, URLError
#Import for creating a directory to store the files in so that we don't end up with a
#       bunch of messy csv files every time we run this thing.
from os import path, makedirs, getcwd
import csv

riottoken = '180d011c-06d3-4722-9eef-3a3de8d6bc83' #My api token for riotgames
folderpath = '/CSV Files' #Local folder for csv files
riotroot = 'https://global.api.pvp.net/api'

fieldnames = ['id', 'name', 'description', 'plaintext']
url = '/lol/static-data/na/v1.2/item?itemListData=colloq&api_key={0}'

if not path.exists(getcwd()+folderpath):
    makedirs(getcwd()+folderpath)

csvfile = open(getcwd()+folderpath+'/item.csv', 'wb')
wr = csv.writer(csvfile, quoting=csv.QUOTE_ALL)

tothecsv = [[]]
for item in fieldnames:
    tothecsv[0].append(item)

response = urlopen(Request(riotroot+url.format(riottoken), headers = {'User-Agent' : 'Magic Browser'})).read().split('data')[1].split('id":')[1:]
i=0
for piece in response:
    if i % 5 == 0:
        print "{0} of {1} items have been processed".format(response.index(piece), len(response))
    i+=1
    temp = []
    temp.append(piece[:4])
    for item in fieldnames[1:]:
        if not piece.find(item) == -1:
            temp.append(piece[piece.find(item)+len(item)+3:piece.find('"', piece.find(item)+ len(item)+3)])
        else:
            temp.append("")
    tothecsv.append(temp)
for item in tothecsv:
    wr.writerow(item)
csvfile.close()
