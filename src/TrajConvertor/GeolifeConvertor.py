def PLTtoCSV(source,destination):
    # convert plt file to csv file
    sf = open(source,"r")
    df = open(destination,"w")

    # ignore 6 first lines
    for i in range(6):
        sf.readline()
    
    # convert
    lns=sf.readlines()
    df.write("latitude,longitude\n")
    for ln in lns:
        sln=ln.split(",")
        df.write(sln[0]+","+sln[1]+"\n")
    
    sf.close()
    df.close()