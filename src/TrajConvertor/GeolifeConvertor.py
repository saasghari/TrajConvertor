import os

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



def GeolifeConvert(src,des):

    files=os.listdir(src)

    # progress bar
    cnt=0   # counter for progress bar
    tn=len(files)  # total number for progress bar

    for fname in files:
        srcfn=src+"/"+fname
        desfn=des+"/T_"+str(cnt)+".csv"
        PLTtoCSV(srcfn,desfn)

        # progress bar
        p=int(cnt*100/tn)
        print("progress...",end=" ")
        print('\033[92m'+str(p)+"%"+'\033[0m', end="\r")
        cnt=cnt+1
    # progress bar
    print("progress...",end=" ")
    print('\033[92m'+"100%"+'\033[0m', end="\r")
