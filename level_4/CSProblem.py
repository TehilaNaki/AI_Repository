# N-queens problem

# The variables' value are in a list of queens' places.
# I.E: If there is a queen in row=1 col=2, then item 1 on the list will be 2.
# If there is no queen in the row, the value is -1
#
# The domains are a list of lists - the domain of every var.
#
# The state is a list of 2 lists: the vars. and the domains.

def create(n):  # the board size is nXn
    d = []  # d is the domains
    # puts the options in the domain
    for i in range(n):
        d += [list(range(n))]
    return [[-1] * n, d]  #[[-1,-1,-1],[[1,2,3],[1,2,3],[1,2,3]]]


def domain(problem, v):  # problem is the state, v is a variable (a row)
    # Returns the domain of v
    return problem[1][v][:]


def domain_size(problem, v):
    # Returns the domain size of v
    return len(problem[1][v])


def assign_val(problem, v, x):
    # Assigns x in var. v
    problem[0][v] = x


def get_val(problem, v):
    # Returns the val. of v
    return problem[0][v]


def erase_from_domain(problem, v, x):
    # Erases x from the domain of v
    problem[1][v].remove(x)


def get_list_of_free_vars(problem):
    # Returns a list of vars. that were not assigned a val.
    l = []
    for i in range(len(problem[0])):
        if problem[0][i] == -1:
            l += [i]
    return l

# check if the problem is solve
def is_solved(problem):
    # Returns True if the problem is solved
    for i in range(len(problem[0])):
        if problem[0][i] == -1:
            return False
    return True

# check if the state is ok
def is_consistent(problem, v1, v2, x1, x2):
    # Returns True if v1=x1 and v2=x2 is consistent with all constraints
    return x1 != x2 and abs(v1 - v2) != abs(x1 - x2)  # x1!=x2 - not on the same col.
    # abs(v1-v2)!=abs(x1-x2) - not on the same diagonal

# delete v from the free vars list
def list_of_influenced_vars(problem, v):
    # Returns a list of vars. whose domain will be
    # influenced by assigning a val. to v
    l = get_list_of_free_vars(problem)
    if v in l:
        l.remove(v)
    return l

# print the board
def present(problem):
    print()
    for r in range(len(problem[0])):
        for c in range(len(problem[0])):
            if problem[0][r] == c:
                print("Q", end="")
            else:
                print("#", end="")
        print()


