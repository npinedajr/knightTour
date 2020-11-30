from collections import deque

def main():
    knightGraph = createKnightGraph()
    print("==========Welcome to Knight's Travails!==========")
    print("If you would like to quit the program, please press enter.")
    while True:
        startingCoordinate = chooseCoordinate("Where would you like the knight to start?","Starting Location: ")
        if startingCoordinate == "":
            break 
        else:
            destination = chooseCoordinate("Where would you like the knight to go?","Destination: ")
            if destination == startingCoordinate:
                while True:
                    print("The destination is the same as the starting coordinate. Please chose a different destination.")
                    destination = chooseCoordinate("Where would you like the knight to go?","Destination: ")
                    if destination != startingCoordinate:
                        break
            if destination == "":
                break
            else:
                shortestPath = knightMovement(startingCoordinate,destination,knightGraph)
                print("")
                print("The shortest path to your destination is the following:")
                for i in range(len(shortestPath)):
                    if i == len(shortestPath)-1:
                        print(shortestPath[i],end="",flush=True)
                    else:
                        print(shortestPath[i],"->",end="",flush=True)
    print("==========Thank you for using Knight's Travails!==========")

def chooseCoordinate(question,inputFrame):
    """
    Inputs: A string named question, which represents the question the user is answering.
            A string named inputFrame, which will hold the frame where the user will input their coordinate.
    Returns: Can return a empty string, which means the user would like to stop using the program.
             Can also return a tuple, which represents the coordinate the user is answering the question with.
    Purpose: To ask the user for a valid coordinate based on the quetion entered into the function. 
    """
    validNumbers = "12345678"
    while True:
        print("")
        print(question)
        coordinate = input(inputFrame)
        if coordinate == "":
            return coordinate
        elif "," in coordinate:
            coordinateList = coordinate.split(",")
            if len(coordinateList) == 2:
                if coordinateList[0].isnumeric() and coordinateList[1].isnumeric():
                    if coordinateList[0] in validNumbers and len(coordinateList[0]) == 1 and coordinateList[1] in validNumbers and len(coordinateList[1]) == 1:
                        coordinateList[0] = int(coordinateList[0])
                        coordinateList[1] = int(coordinateList[1])
                        validCoordinate = (coordinateList[0],coordinateList[1])
                        return validCoordinate
                    else:
                        print("Invalid entry. The x and y coordinates must be a value from 0 to 8.")
                else:
                    print("Invalid entry. This coordinate must be numeric.")
            else:
                print("Invalid entry. This coordinate must be two-dimensional.")
        else:
            print("Invalid entry. Please seperate the x and y value with a comma.")

def knightMovement(startingCoordinate,destination,knightGraph):
    """
    Inputs: A tuple named startingCoordinate, which represents the position the knight will begin its journey from.
            A tuple named destination, which represents the position the knight will arrive to.
            A graph that holds all the possible moves a knight can make from each position in the 8x8 board.
    Returns: A list of tuples, which represents the coordinates the knight will go through to reach the destination in the shortest 
             amount of moves possible.
    Purpose: To obtain the shortest path possible that the knight will take to go from its starting position to its destination. 
    """
    shortestPath = deque()
    queue = deque()
    queue.append(startingCoordinate)
    knightGraph[startingCoordinate][1] = True 
    while True:
        current = queue.popleft()
        if current == destination:
            shortestPath.appendleft(current)
            while True:
                shortestPath.appendleft(knightGraph[current][2])
                current = knightGraph[current][2]
                if current == startingCoordinate:
                    break
            for i in range(8):
                for j in range(8):
                    coordinate=(i+1,j+1)
                    knightGraph[coordinate][1] = False
                    if knightGraph[coordinate][2] != (-1,-1):
                        knightGraph[coordinate][2] = (-1,-1)
            return shortestPath
        neighbors = knightGraph[current][0]
        for i in range(len(neighbors)):
            if knightGraph[neighbors[i]][1] == False:
                queue.append(neighbors[i])
                knightGraph[neighbors[i]][1] = True
                knightGraph[neighbors[i]][2] = current

def createKnightGraph():
    """
    Inputs: None
    Returns: A graph, which is presented as a dictionary, that holds all possible moves.
             the knight can make from each position on a 8x8 board. The value of each item pair
             consists of a list, where the first element contains all possible moves that can be 
             made from the coordinate entered as the key, the second element indicates whether the
             coordinate has been visited, and the third element indicates the coordinate visited 
             before arrive to the coordinate in the key. By default, all coordinates have their previous
             coordinate as (-1,-1).
    Purpose: To create a graph with all of the possible moves a knight can make on a 8x8 board. 
    """
    knightGraph= {}
    for i in range(8):
        for j in range(8):
            coordinate = (i+1,j+1)
            possibleMoves = findPossibleMoves(coordinate)
            knightGraph[coordinate] = [possibleMoves,False,(-1,-1)]
    return knightGraph

def findPossibleMoves(coordinate):
    """
    Inputs: A tuple, which represents a position on the 8x8 board.
    Returns: A list of all valid moves a knight can make from the position entered in the function.
    Purpose: To obain a list of all the possible moves a knight can take from the coordinate entered into the function. 
    """
    possibleMoves = []
    deltaX = [1,1,-1,-1,2,2,-2,-2]
    deltaY = [2,-2,2,-2,1,-1,1,-1]
    for i in range(len(deltaX)):
        if 8>=(coordinate[0]+deltaX[i])>=1 and 8>=(coordinate[1]+deltaY[i])>=1:
            temp = (coordinate[0]+deltaX[i],coordinate[1]+deltaY[i])
            possibleMoves.append(temp)
        else:
            continue 
    return possibleMoves

main()
