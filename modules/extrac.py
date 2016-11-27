from bs4 import BeautifulSoup
import urllib2


synopses_imdb =[]
with open('/Users/raghav/Downloads/ml-latest-small/links.csv','r') as fp:
    i = 0
    for line in fp:
        if i == 0:
            i+=1
            continue
        else:
            lis = line.split(',')
            link = "http://www.imdb.com/" + "title/tt" + str(lis[1]) + "/synopsis?ref_=tt_stry_pl"
            #print link
            request = urllib2.Request(str(link))
            response = urllib2.urlopen(request)
            soup = BeautifulSoup(response, "html.parser")
        for div in soup.findAll('div', {'id': 'swiki.2.1'}):
            #print div.text
            synopses_imdb.append(div.text)
        i+=1
        print i
        if i == 225:
            break
synopses_list = open('synopses_list_imdb_mod.txt', 'w')

for item in synopses_imdb:
     synopses_list.write("%s\n BREAKS HERE" % item.encode('utf-8'))

synopses_list.close()
