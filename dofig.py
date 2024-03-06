import os
import matplotlib.pyplot as plt


def dofig():
    global sendsynthesis
    
    birds = []
    birdscount = []
    logcount = 0
    run = True

    while run:
        if os.path.exists("logs/log"+str(logcount)+".log"):
            f = open("logs/log"+str(logcount)+".log","r")
            
            for line in f.readlines():
                if not erasedate(line.replace("\n","")) in birds:
                    birds.append(erasedate(line.replace("\n","")))
                    birdscount.append(1)
                else:
                    birdscount[birds.index(erasedate(line.replace("\n","")))] += 1
            logcount +=1
        else:
            run = False



    

    fig, ax = plt.subplots()
    
    
    ax.pie(birdscount, labels=birds)
    
    
    plt.show(block=True)
        


dofig()
        
        