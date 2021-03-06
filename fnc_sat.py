import itertools

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

def main():
    expr = input()
    # create dict
    varDict, clausesNo, varNo = createVarDict(expr)
    # create matrix
    matrix = createMatrix(expr, varDict, clausesNo, varNo)
    # create a list of list of all combinations of 0 and 1 of length equal to varNo
    combinations = [list(i) for i in itertools.product([0, 1], repeat=varNo)]
    # analyse each interpretation
    for interpr in combinations:
        trueClauses = 0
        for i in range(0,clausesNo):
            falseVarNo = 0
            for j in range(0, varNo):
                #condition for a clause to be true
                if (matrix[i][j] == 1 and interpr[j] == 1) or (matrix[i][j] == 2 and interpr[j] == 0):
                    trueClauses += 1
                    break
                else:
                    falseVarNo += 1
            # stop if all clauses are false
            if falseVarNo == varNo:
                break
        # stop if solution is found
        if trueClauses == clausesNo:
            print(1)
            return 0
    print(0)
    return 0
    
main()
