# queues.py
import math
from numbers import Number

import queues_utilities

# fixme - add info to docstring
# fixme - add parameter types and return types

def is_valid(lamda, mu: float, c: int = 1) -> bool:
    """

    :param lamda:
    :param mu:
    :param c:
    :return:
    """
    print(f'is_valid({lamda},{mu},{c})')

    # fixme account for non numeric values, tuples
    # fixme - maybe use list comp loop with helper function lamda_j_valid()

    # is c or mu valid

    is_mu_num = isinstance(mu, Number)
    print(f'is_mu_num: {is_mu_num}')
    is_c_num = isinstance(mu, Number)
    print(f'is_c_num: {is_c_num}')

    if (c <= 0 or mu <=1):
        #print('c or mu invalid')
        return False



    # if tuple
        # fixme - list comp through lamda checking is instance using all or any, from numbers import Number, if any(var, Number)
    # if not tuple
        # fixme - check if a value is numeric: from numbers import Number,

    # is lamda tuple

    is_lamda_num = isinstance(lamda, Number)
    print(f'is_lamda_num: {is_lamda_num}')

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

def is_feasible(lamda, mu: float, c: int = 1) -> bool:
    """

    :param lamda:
    :param mu:
    :param c:
    :return:
    """
    print(f'is_feasible({lamda},{mu},{c})')

    # fixme account for non numeric values, tuples

    # check is_valid
    is_valid_res = is_valid(lamda,mu,c)
    if (is_valid_res != True):
        return False

    # calc lamda_new
    lamda_new = queues_utilities.calc_lamda_agg(lamda)

    # calc ro
    ro = lamda_new / (c * mu)
    #print(f'ro = {ro}')

    # fixme - use "in range"

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

def calc_p0(lamda, mu: float, c: int = 1) -> float:
    """

    :param lamda:
    :param mu:
    :param c:
    :return:
    """
    print(f'calc_p0({lamda},{mu},{c})')

    # check is_valid
    is_valid_res = is_valid(lamda,mu,c)
    if (is_valid_res != True):
        return False

    # check is_feasible
    is_feasible_res = is_feasible(lamda,mu,c)
    if (is_feasible_res != True):
        return False

    # all([instance(x,Number) for x in lamda]))
    # calc lamda_new
    lamda_new = queues_utilities.calc_lamda_agg(lamda)

    # calc ro
    ro = lamda_new / (c * mu)
    print(f'ro = {ro}')


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
    n = 0

    # TODO sum term1
    # sum term1

    print(f'c {c}')

    for n in range(1, c+1):
        print(f'n = {n}')
        term1 = term1 + (r**n)/math.factorial(n)
        print(f'term1 = {term1}')




    # calc p0
    #p0 = 1 / (term1 + term2)
    p0 = 5
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


def calc_lq_mmc(lamda, mu: float, c: int = 1) -> float:
    """

    :param lamda:
    :param mu:
    :param c:
    :return:
    """
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
    # fixme - check for mm1, calc lq mm1
        # else - calc lq mmc
    # fixme - make and use calc lq mm1 function
    # check c
    if (c == 1):
        lq = lamda_new ** 2 / (mu * (mu-lamda_new))
        print(f'lq = {lq}')
        return lq

    # calc r
    r = lamda_new / mu
    print(f'r = {r}')

    # fixme finish p0
    # p0 = calc_p0(lamda_new, mu, c)

    # qs - figure out factorials
    lq_mmc = (lamda_new**2) / (mu * (mu - lamda_new))
    print(f'lq_mmc = {lq_mmc}')
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

def calc_bk_mmc(k: int, lamda, mu: float, c: int = 1) -> float:
    """

    :param k:
    :param lamda:
    :param mu:
    :param c:
    :return:
    """
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

def calc_wqk_mmc(k: int, lamda, mu: float, c: int = 1) -> float:
    """

    :param k:
    :param lamda:
    :param mu:
    :param c:
    :return:
    """
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

def calc_lqk_mmc(k: int, lamda, wqk: float, c: int = 1) -> float:
    """

    :param k:
    :param lamda:
    :param wqk:
    :param c:
    :return:
    """
    print(f'calc_bk_mmc({k},{lamda},{wqk},{c})')

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

def use_littles_law(lamda, mu, c=1, **kwargs) -> dict:
    """

    :param lamda:
    :param mu:
    :param c:
    :param kwargs:
    :return:
    """
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








