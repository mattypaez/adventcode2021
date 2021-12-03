def getList():
    with open("d1.txt", "r") as file:
        lines = file.readlines()
        strippedLines = [int(line.strip()) for line in lines]
        return strippedLines

# Part 1:
def getIncreases():
    sonarList = getList()
    previousMeasurement = None
    count = 0
    for measurement in sonarList:
        if previousMeasurement != None:
            if previousMeasurement < measurement:
                count += 1
        previousMeasurement = measurement
    
    print(count)

# Part 2:
def getWindowIncreases():
    sonarList = getList()
    count = 0
    for i in range(len(sonarList)):
        try:
            firstSum = sonarList[i] + sonarList[i+1] + sonarList[i+2]
            nextSum = sonarList[i+1] + sonarList[i+2] + sonarList[i+3]
            if firstSum < nextSum:
                count += 1
        except:
            continue

    print(count)




    
getIncreases()
getWindowIncreases()