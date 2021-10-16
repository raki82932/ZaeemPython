def sortByArtist(filename,artist):
    f = open(filename,'r')
    data = f.read().splitlines()
    data.pop(0)
    filtered_data = list(filter(('').__ne__,data))
    l=[]
    for i in range(2,len(filtered_data),3):
        if filtered_data[i]==artist:
            l.append(filtered_data[i-2])
    return l


def  genreFilter(filename):
    f = open(filename,'r')
    data = f.read().splitlines()
    data.pop(0)
    filtered_data = list(filter(('').__ne__,data))
    d={}
    for i in range(1,len(filtered_data),3):
        if filtered_data[i] not in d:
            d[filtered_data[i]]=[filtered_data[i-1]]
        else:
            d[filtered_data[i]].append(filtered_data[i-1])
    return d


def sortByGenre(filename:str,genere:str,outputfilename:str) -> None:
    f = open(filename,'r')
    data = f.read().splitlines()
    data.pop(0)
    filtered_data = list(filter(('').__ne__,data))
    output_file = open(outputfilename,'w')
    output_file.write(genere + "\n")
    j = 0
    for i in range(1,len(filtered_data),3):
        if filtered_data[i] == genere:
            j+=1
            s="{}. {} - {}\n".format(j,filtered_data[i-1],filtered_data[i+1])
            output_file.write(s)

            

