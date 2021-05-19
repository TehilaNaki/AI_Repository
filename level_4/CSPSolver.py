'''
Tehila Naki-323071571
Merav Berkowitz (Izhaki)-322915430
'''

import math
import CSProblem
import copy

def solve(n):
    CSProblem.present(backtrack(CSProblem.create(n)))


def backtrack(p):
    var = next_var(p, MRV=True)  # MRV-Most constrained variable or Minimum Remaining Values
    if var == None:
        return p
    dom = sorted_domain(p, var, LCV=True)  # LCV-least constraining value
    for i in dom:
        bu = copy.deepcopy(p)
        CSProblem.assign_val(bu, var, i)
        propagate_constraints(bu, var)  # delete the optione after choose i
        bu = backtrack(bu)
        if CSProblem.is_solved(bu):
            return bu
    return p

'''
The function sort the domain by LCV
'''
def sorted_domain(p, var, LCV=True):
    if LCV == False:
        return CSProblem.domain(p, var)

    dom = []
    # for each option in the domain of var
    for item in p[1][var]:
        p1 = copy.deepcopy(p)
        # insert item into var index
        CSProblem.assign_val(p1, var, item)
        # count the changes after assign val
        dif = num_of_del_vals([p1, var, item])
        # insert to the list like dict for sort
        dom.insert(0,[item, dif])
    # sort the dict by the key- second value:the option deleted
    sort = sorted(dom, key=second)
    # return the index after sort
    return [i[0] for i in sort]

'''
Help function for sort
'''
def second(p):
    return p[1]


# return the num of options deleted from domain
def num_of_del_vals(l):
    # l=[problem, the variable, the val. assigned to the var.]
    # returns the num. of values. erased from vars domains after assigning x to v
    count = 0
    for inf_v in CSProblem.list_of_influenced_vars(l[0], l[1]):
        for i in CSProblem.domain(l[0], inf_v):
            if not CSProblem.is_consistent(l[0], l[1], inf_v, l[2], i):
                count += 1
    return count

'''
Function return the next val by MRV
'''
def next_var(p, MRV=True):
    # p is the problem
    # MRV - Minimum Remained Values
    # Returns next var. to assign
    # If MRV=True uses MRV heuristics
    # If MRV=False returns first non-assigned var.
    if MRV == False:
        v = CSProblem.get_list_of_free_vars(p)
        if v == []:
            return None
        else:
            return v[0]
    # make a list of the len-domain
    lens = [len(item) for item in p[1]]
    # set the start value
    index=None
    min=math.inf
    # for each item in the len list
    for i in range(len(lens)):
        # check if not set and minimum
        if(p[0][i]==-1 and lens[i]<min):
            min =lens[i]
            index=i
    return index

# delete the forbidden options from domain
def propagate_constraints(p, v):
    for i in CSProblem.list_of_influenced_vars(p, v):
        for x in CSProblem.domain(p, i):
            if not CSProblem.is_consistent(p, i, v, x, CSProblem.get_val(p, v)):
                CSProblem.erase_from_domain(p, i, x)


solve(5)
