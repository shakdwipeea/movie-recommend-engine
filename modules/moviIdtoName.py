mov = {}
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
#print(mov)
def getMovieNames(movieId):
    return mov[movieId]
