mov = {}
movL = {}
with open('/Users/raghav/Downloads/ml-latest-small/movies.csv', 'r') as fp:
    i = 0
    for line in fp:
        if i == 0:
            i+=1
            continue
        else:
            movLis = line.split(',')
            mov[movLis[0]] = movLis[1]
            if i == 186:
                break
        i+=1

with open('modules/title_list_mod.txt', 'r') as fp:
    i = 0
    for line in fp:
        if i == 0:
            i+=1
            continue
        else:
            movLis = line.split(',')
            movL[str(movLis[0])] = i
            if i == 186:
                break
        i+=1
#print(mov)
def getMovieNames(movieId):
    return mov[movieId]


def getMovieId(movieName):
    return movL[str(movieName)]
