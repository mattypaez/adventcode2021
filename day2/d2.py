def getList():
    with open("d2.txt", "r") as file:
        lines = file.readlines()
        strippedLines = [line.strip().split(" ") for line in lines]  # This splits the command and value into a list of lists
        return strippedLines

def getPositions1():
    commandList = getList()
    depth = 0
    position = 0
    for i in range(len(commandList)):
        if commandList[i][0] == "forward":
            position += int(commandList[i][1])
        elif commandList[i][0] == "down":
            depth += int(commandList[i][1])
        elif commandList[i][0] == "up":
            depth -= int(commandList[i][1])
    print(depth*position)

def getPositions2():
    commandList = getList()
    depth = 0
    position = 0
    aim = 0
    for i in range(len(commandList)):
        if commandList[i][0] == "forward":
            position += int(commandList[i][1])
            depth += aim * int(commandList[i][1])
        elif commandList[i][0] == "down":
            aim += int(commandList[i][1])
        elif commandList[i][0] == "up":
            aim-= int(commandList[i][1])
    print(depth*position)

getPositions1()
getPositions2()