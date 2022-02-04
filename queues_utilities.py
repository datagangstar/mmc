# queues_utilities.py


# calc_lamda_agg
#
# Description:
# Calculates lamda_agg given a scalar or tuple.
#
# Parameters:
# lamda - arrival rate (scalar or tuple)

# todo - add to queues

def calc_lamda_agg(lamda: float) -> int:
    """

    :param lamda:
    :return:
    """
    print(f'calc_lamda_agg({lamda})')

    # is lamda scalar, return scalar
    if (type(lamda) is not tuple):
        return lamda

    # sum lamda_agg
    lamda_agg = sum([lamda_j for lamda_j in lamda])

    return lamda_agg
