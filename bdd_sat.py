# simple tree node strucutre
class Node:
    def __init__(self, data):
        self.left = []
        self.right = []
        self.data = data

# return mapping of variables to consecutive numbers
# number of variables and clauses
def createVarDict(expr):
    varDict = {}
    clauses = expr.split('^')
    clausesNo = len(clauses)
    varNo = 0
    # parse each clause
    for clause  in clauses:
        clause = clause[1:-1]
        # split clause into variables
        variables = clause.split('V')
        for x in variables:
            # remove negation sign
            if x[0] == '~':
                x = x[1:]
            # assign value in dict
            if x not in varDict:
                varDict[x] = varNo
                varNo += 1
    return varDict, clausesNo, varNo

# return a matrix where each line is a clause and each column
# represents a variable from x0 to xn-1
def createMatrix(expr, varDict, clausesNo, varNo):
    # initialize matrix wih zeroes
    matrix = []
    for i in range(0,clausesNo):
        matrix.append([])
        for j in range(0, varNo):
            matrix[i].append(0)
    crtClause = 0
    clauses = expr.split('^')
    # parse each clause of expression
    for clause  in clauses:
        clause = clause[1:-1]
        variables = clause.split('V')
        for x in variables:
            # if a variable appears negated, encode it with 2
            # else with 1
            if x[0] == '~':
                x = x[1:]
                # look up the variable in the dict 
                if x in varDict:
                    matrix[crtClause][varDict[x]] = 2
            else:
                if x in varDict:
                    matrix[crtClause][varDict[x]] = 1
        crtClause += 1
    return matrix

# checks if a solution is found
def evaluateLeftNode(parent, crtVar):
    child = parent.left
    parentMatrix = parent.data
    clauseNo = len(parentMatrix)
    # add just the clauses that are not affected by the current valuable
    for i in range(0, clauseNo):
        if parentMatrix[i][crtVar] != 2:
            child.data.append(parentMatrix[i])
    # if all clauses are simplified => solution found
    if len(child.data) == 0:
        return 1
    return 0

# checks if a solution is found
def evaluateRightNode(parent, crtVar):
    child = parent.right
    parentMatrix = parent.data
    clauseNo = len(parentMatrix)
    # add just the clauses that are not affected by the current valuable
    for i in range(0, clauseNo):
        if parentMatrix[i][crtVar] != 1:
            child.data.append(parentMatrix[i])
    # if all clauses are simplified => solution found
    if len(child.data) == 0:
        return 1
    return 0

def createTree(parent, crtVar, varNo, solFound):
    # stop if number of variable is  reached
    if crtVar >= varNo:
        return
    # create and evaluate left child 
    leftChild = Node([])
    parent.left = leftChild
    solFound = evaluateLeftNode(parent, crtVar)
    if solFound == 1:
        # add 1 to solution vector
        x.append(1)
        return 
    else:
        # continue to create tree recursively
        createTree(leftChild, crtVar + 1, varNo, solFound)
        # create and evaluate right child
        rightChild = Node([])
        parent.right = rightChild
        solFound = evaluateRightNode(parent, crtVar)
        # if solution is found add 1 to the vector
        if solFound == 1:
            x.append(1)
            return 
        else:
            # continue to create tree recursively
            createTree(rightChild, crtVar + 1, varNo, solFound)
        return 
x = [0]
def main():
    expr = input()
    # create dict
    varDict, clausesNo, varNo = createVarDict(expr)
    # create matrix of variables
    matrix = createMatrix(expr, varDict, clausesNo, varNo)
    # assign all variables matrix to root node
    root = Node(matrix)
    createTree(root, 0, varNo, 0)
    print(x[-1])
main()
