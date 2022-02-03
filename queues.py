# queues.py


# test sheet
# https://upedu.sharepoint.com/:x:/r/sites/GRP-Python-22/_layouts/15/Doc.aspx?sourcedoc=%7B5C6DEF46-23C0-4E95-8D91-3E87D403AA9B%7D&file=example%20just%20values.xlsx&action=default&mobileredirect=true


# queues_tests.py - Python program you wrote to verify that your functions (from queues.py) satisfy the requirements and function correctly

# queues.py – Each of the following functions (as described for Project 1) should be implemented in your queues.py:

# TODO when we declare functions, we can offer type hints - we should always use type hints when specific types are expected.

# is_valid( lamda, mu, c=1)
# is_feasible(lamda1, mu, c=1)
# calc_p0(lamda, mu, c=1)
# calc_lq_mmc(lamda, mu, c=1)
# calc_bk_mmc(k, lamda, mu, c=1)
# calc_wqk_mmc(k, lamda, mu, c=1)
# calc_lqk_mmc(k, lamda, wqk, c=1)
# use_littles_law(lamda, mu, c=1, **kwargs)



# is_valid
#
# Description:
#
#
# Parameters:
# lamda - arrival rate (scalar or tuple)
# mu - service rate
# c - # of servers
#
# Return:
# boolean
import queues_utilities


def is_valid(lamda, mu, c=1):
    print(f'is_valid({lamda},{mu},{c})')

    # TODO - maybe use list comp loop with helper function lamda_j_valid()

    # is c or mu valid
    if (c <= 0 or mu <=1):
        #print('c or mu invalid')
        return False

    # is lamda tuple
    if (type(lamda) is not tuple):
        # is lamda scalar valid
        if (lamda <= 0):
            #print('lamda scalar invalid')
            return False
    else:
        # is lamda tuple element valid
        for lamda_j in lamda:
            if (lamda_j <= 0):
                #print(f'lamda tuple {lamda_j} invalid')
                return False

    return True



# is_feasible
#
# Description:
#
#
# Parameters:
# lamda - arrival rate (scalar or tuple)
# mu - service rate
# c - # of servers

def is_feasible(lamda, mu, c=1):
    print(f'is_feasible({lamda},{mu},{c})')

    # check is_valid
    is_valid_res = is_valid(lamda,mu,c)
    if (is_valid_res != True):
        return False

    # calc lamda_new
    lamda_new = queues_utilities.calc_lamda_agg(lamda)

    # calc ro
    ro = lamda_new / (c * mu)
    #print(f'ro = {ro}')

    # TODO - Do we have to do something like "in range"
    # todo - settings add fixme, look up adding todo tags

    # check ro
    if (ro >= 1):
        return False

    return True





# calc_p0
#
# Description:
#
#
# Parameters:
# lamda - arrival rate (scalar or tuple)
# mu - service rate
# c - # of servers

def calc_p0(lamda, mu, c=1):
    print(f'calc_p0({lamda},{mu},{c})')

    # check is_valid
    is_valid_res = is_valid(lamda,mu,c)
    if (is_valid_res != True):
        return False

    # check is_feasible
    is_feasible_res = is_feasible(lamda,mu,c)
    if (is_feasible_res != True):
        return False

    # TODO - if tuple
    # calc lamda_new
    lamda_new = queues_utilities.calc_lamda_agg(lamda)

    # calc ro
    ro = lamda_new / (c * mu)
    print(f'ro = {ro}')

    # TODO handle p0 = 0.19999999999999996, use is close
    # check c
    if (c <= 1):
        p0 = 1 - ro
        print(f'p0 = {p0}')
        return p0

    # calc r
    r = lamda_new / mu
    print(f'r = {r}')

    # initialize term1
    term1 = 0

    # TODO sum term1
    # sum term1
    # for n = 0 to c-1:
    #     term1 = term1 + r**n/n!
    #
    #

    # calc term
    term2 = r**c

    # calc p0
    p0 = 1 / (term1 + term2)
    return p0


# calc_lq_mmc
#
# Description:
#
#
# Parameters:
# lamda - arrival rate (scalar or tuple)
# mu - service rate
# c - # of servers

def calc_lq_mmc(lamda, mu, c=1):
    print(f'calc_lq_mmc({lamda},{mu},{c})')

    # check is_valid
    is_valid_res = is_valid(lamda,mu,c)
    if (is_valid_res != True):
        return False

    # check is_feasible
    is_feasible_res = is_feasible(lamda,mu,c)
    if (is_feasible_res != True):
        return False

    # TODO - if tuple
    # calc lamda_new
    lamda_new = queues_utilities.calc_lamda_agg(lamda)

    # calc ro
    ro = lamda_new / (c * mu)
    print(f'ro = {ro}')

    # TODO check 3.2 is correct, adapt test case sheet from example sheet
    # todo - make and use calc lq mm1 function
    # check c
    if (c == 1):
        lq = lamda_new ** 2 / (mu * (mu-lamda_new))
        print(f'lq = {lq}')
        return lq

    # calc r
    r = lamda_new / mu
    print(f'r = {r}')

    # TODO finish p0
    # p0 = calc_p0(lamda_new, mu, c)

    # TODO figure out factorials
    # lq = ( (r**c) * ro ) / c!(1-ro)**2 ) * p0
    lq = 4

    # import math
    #
    # print(f"The factorial of {m} is : ")
    # print(math.factorial(m))

    return lq




# calc_bk_mmc
#
# Description:
#
#
# Parameters:
# k -
# lamda - arrival rate (scalar or tuple)
# mu - service rate
# c - # of servers

def calc_bk_mmc(k, lamda, mu, c=1):
    print(f'calc_bk_mmc({k},{lamda},{mu},{c})')

    return False



# calc_wqk_mmc
#
# Description:
#
#
# Parameters:
# k -
# lamda - arrival rate (scalar or tuple)
# mu - service rate
# c - # of servers

def calc_wqk_mmc(k, lamda, mu, c=1):
    print(f'calc_bk_mmc({k},{lamda},{mu},{c})')

    return False


# calc_lqk_mmc
#
# Description:
#
#
# Parameters:
# k -
# lamda - arrival rate (scalar or tuple)
# wqk
# c - # of servers

def calc_lqk_mmc(k, lamda, wqk, c=1):
    print(f'calc_bk_mmc({k},{lamda},{mu},{c})')

    return False



# use_littles_law
#
# Description:
#
#
# Parameters:
# lamda - arrival rate (scalar or tuple)
# mu - service rate
# c - # of servers
# **kwargs

def use_littles_law(lamda, mu, c=1, **kwargs):
    print(f'calc_bk_mmc({lamda},{mu},{c},{kwargs})')


    lamda_agg = 20
    mu = 25
    c = 1
    r = lamda_agg / mu
    print(f'r: {r}')
    ro = lamda_agg / (c * mu)
    print(f'ro: {ro}')

    print()

    kwargs = {"Lq": 3.2}
    # kwargs = {"L": 5.7}
    # kwargs = {"Wq": 0.16}
    # kwargs = {"w": 8.4}
    print(kwargs)

    # check if kwargs exists
    if not type(kwargs) is dict:
        print("kwargs is  empty")

    else:
        print("kwargs is not empty")

    print()

    # get key and value from kwargs
    key = list(kwargs.keys())[0]
    value = list(kwargs.values())[0]
    print(f'key: {key}')
    print(f'value: {value}')
    key = key.lower()
    print(f'keylower: {key.lower()}')

    print()

    lq = 0
    l = 0
    wq = 0
    w = 0

    # check key metric and calc lq
    if key == "lq":
        print(f'we have key: {key}')
        lq = value

    if key == "l":
        print(f'we have key: {key}')
        l = value
        lq = 1 - r

    if key == "wq":
        print(f'we have key: {key}')
        wq = value
        lq = wq * lamda_agg

    if key == "w":
        print(f'we have key: {key}')
        w = value
        lq = (lamda_agg * w) - r

    # get remaining metrics
    l = lq + r
    wq = lq / lamda_agg
    w = l / lamda_agg

    print()
    print('done')
    print(f'lq: {lq}')
    print(f'l: {l}')
    print(f'wq: {wq}')
    print(f'w: {w}')

    return False

 # ------------------------------------








