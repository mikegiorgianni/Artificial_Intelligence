from __future__ import print_function
import random

#initialState = ("1" * 4) + ("0" * 3) + ("1" * 2) + ("0" * 5) + ("1" * 2)
initialState = ("1" * 6) + "0" + ("1" * 9)
testState = "0000100100101100"
goalState = ("0" * 6) + "1" + ("0" * 9)

# Assignment Link
# https://www.cs.drexel.edu/~popyack/Courses/AI/Sp19/assignments/HW1/index.html#Prog 
# A rule r can be characterized by the attributes (jumper, goner, newpos), which respectively refer to the position of a peg that is about to jump (jumper), 
# the position of the peg it jumps over (goner), and the new position of the jumper (newpos). The rule is defined by the following action and preconditions:

# Action:  change values in state s of jumper position to 0, goner position to 0, and newpos position to 1.
# Precondition: values of jumper, goner, newpos positions are respectively 1, 1, and 0.

def goal(state):
    if state == goalState:
        return True
    else:
        return False

# A rule r can be characterized by the attributes (jumper, goner, newpos)
def applyRule(rule, state):
    state = setPos(state, rule[0], "0")
    state = setPos(state, rule[1], "0")
    state = setPos(state, rule[2], "1")
    return state

#state, position, value
def setPos(s, pos, val):
    x = s[0:-(pos+1)] + val + s[-pos:]
    return x

def getPos(s, pos):
    x = s[-(pos+1)]
    return x

def precondition(rule, state):
    # THE LOOP ITERATIONS ARE IMPORTANT NOTEBOOK IT LATER
    for condition in rule:
        if condition < 0 or condition > 15:
            return False
    # SANITY CHECKS
    #print(rule[0])
    #print(state)
    if getPos(state, rule[0]) != "1":
        return False
    if getPos(state, rule[1]) != "1":
        return False
    if getPos(state, rule[2]) != "0":
        return False
    if (rule[1]//4 - rule[0]//4) != (rule[2]//4 - rule[1]//4): #row
        return False
    if (rule[1]%4 - rule[0]%4) != (rule[2]%4 - rule[1]%4): #col
        return False
    
        
    delta = rule[1]-rule[0]
    
    if abs(delta) in [1, 3, 4, 5]:
        return True
    else:
        return False

def applicableRules(state):
    ruleList = []
    dRange = [-1, 1, -3, 3, -4, 4, -5, 5]
    for pos in range(16):
        for delta in dRange:
            rule = (pos, pos + delta, pos + delta + delta)
            if precondition( rule, state ) == True:
                ruleList.append(rule)
    return ruleList

def describeState(state):
    for row in range(3,-1,-1):
        for col in range(3,-1,-1):
            if getPos(state, (row * 4) + col) == "1":
                print("x", end=" ")
            else:
                print("o", end=" ")
        print()
        
def conv(num):
    if num < 10:
        return str(num)
    else:
        return chr((num - 10) + ord('A'))
  
          
def describeRule(rule):
    print("The peg in slot " + conv(rule[0]) + " jumps over the peg in slot " + conv(rule[1]) + " and lands in slot " + conv(rule[2]))
        
      

def flailWildly(state):
    if goal(state) == True:
        print("No further moves required \n")
        describeState(state)
        return True
    validRules = applicableRules(state)
    while len(validRules) > 0:
        move = random.choice(validRules)
        validRules.remove(move)
        newState = applyRule(move, state)
        describeRule(move)
        describeState(state)
        if flailWildly(newState) == True:
            return True
    return False

  
def backTrack(stateList):
    state = stateList[0]
    if goal(state) == True:
        return []
    validRules = applicableRules(state)
    if validRules == []:
        return False
    for rule in validRules:
        newState = applyRule(rule, state)
        newStateList = [newState] + stateList
        path = backTrack (newStateList)
        describeState(state)
        if path != False:
            return path + [rule]
    return False
  

print("This is the inital State: ")
describeState(initialState)
print("~~~~~~~~~~~")
##print(backTrack([testState]))
flailWildly(testState)
#print(initialState)