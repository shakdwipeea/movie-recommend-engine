from bs4 import BeautifulSoup
import urllib2

imdb_list = []

with open('/Users/raghav/Downloads/ml-latest-small/links.csv','r') as fp:
    i = 0
    for line in fp:
        if i == 0:
            i+=1
            continue
        else:
            lis = line.split(',')
            link = "http://www.imdb.com/" + "title/tt" + str(lis[1])
            #print link
            request = urllib2.Request(str(link))
            response = urllib2.urlopen(request)
            soup = BeautifulSoup(response, "html.parser")
            x = soup.find('h1', {'itemprop' : 'name'})
            print x.text
            #break
            imdb_list.append(x.text)
        i+=1
        print i
        if i == 200:
            break
synopses_list = open('title_list_mod.txt', 'w')

for item in imdb_list:
     synopses_list.write("%s\n" % item.encode('utf-8'))

synopses_list.close()
