import random

wordList = ["Apple", "Orange", "Monkey", "Dog", "Beach", "Sunset"]

# creating 10 x 10 empty grid

emptyGrid = []
for i in range(10):
    newRow = [" "] * 10
    emptyGrid.append(newRow)

initialState = ( emptyGrid, wordList )

def goal(state):
    if len(state[1]) == 0:
        return True
    else:
        return False

def applyRule(rule, state):
    grid = []
    for row in state[0]:
        grid.append(row[:])
        # creating copy of the wordlist
    List = state[1][:]
    word, row, col, dh, dv = rule[0], rule[1], rule[2], rule[3], rule[4]
    for char in word:
        grid[row][col] = char
        row += dv
        col += dh
    List.remove(word)
    newState = ( grid, List )
    return newState

def precondition( rule, state ):
    word, row, col, dh, dv = rule[0], rule[1], rule[2], rule[3], rule[4]
    # state[0] is emptyGrid and state[1] is the wordList
    grid = state[0]
    List = state[1]
    if dh == dv == 0:
        return False
      #check start pos for row and col of the word
    elif row < 0 or row >= len(grid):
        return False
    elif col < 0 or col >= len(grid[row]):
        return False
      #check ending pos for row and col
    elif row + (len(word)-1) * dv < 0 or row + (len(word)-1) * dv >= len(grid):
        return False
    elif col + (len(word)-1) * dh < 0 or col + (len(word)-1) * dh >= len(grid[row]):
        return False
    for char in word:
        if grid[row][col] != char and grid[row][col] != " ":
            return False
        row += dv
        col += dh
    return True

#rule = (word, row, col, dh, dv)

def generateRules(state):
    ruleList = []
    wordList = state[1]
    grid = state[0]
    dRange = [-1, 0, 1]
    for word in wordList:
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                for dh in dRange:
                    for dv in dRange:
                        rule = (word, row, col, dh, dv)
                        if precondition( rule, state ) == True:
                            ruleList.append(rule)
    return ruleList

def describeState(state):
    for row in state[0]:
        print(row)
    print(state[1])

def describeRule(rule):
    word, row, col, dh, dv = rule[0], rule[1], rule[2], rule[3], rule[4]
    print("Place the word \"" + word + "\" in the grid starting position (" + str(row) + ", " + str(col) + ") and proceeding in the direction [" + str(dh) + ", " + str(dv) + "].")

def flailWildly(state):
    if goal(state) == True:
        describeState(state)
        return True
    validRules = generateRules(state)
    while len(validRules) > 0:
        move = random.choice(validRules)
        validRules.remove(move)
        newState = applyRule(move, state)
        describeState(state)
        describeRule(move)
        #print(validRules)
        if flailWildly(newState) == True:
            return True
    return False

flailWildly(initialState)